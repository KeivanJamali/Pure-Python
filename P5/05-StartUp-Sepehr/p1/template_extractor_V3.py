from pyautocad import Autocad
from tqdm.auto import tqdm
import pythoncom
import time
import os.path

standard_colors = {
    1: (255, 0, 0),    # Red
    2: (255, 255, 0),  # Yellow
    3: (0, 255, 0),    # Green
    4: (0, 255, 255),  # Cyan
    5: (0, 0, 255),    # Blue
    6: (255, 0, 255),  # Magenta
    7: (255, 255, 255),# White
    8: (0, 0, 0),      # Black
    # Add more standard colors as needed
}

standard_line_types = {
    'Continuous': 'Continuous',
    'HIDDEN': 'HIDDEN',
    'Dashed': 'Dashed',
    'Dotted': 'Dotted'
}

class Extract_template():
    def __init__(self, file_name, time_load=30):
        pythoncom.CoInitialize()
        self.acad = Autocad(create_if_not_exists=True)
        self.acad.app.Visible = True
        self.file_path = file_name
        self.acad.app.Documents.Open(self.file_path)
        time.sleep(time_load)

    def _generate_entity_code(self, entity):
        try:
            if hasattr(entity, 'Color'):
                original_color = entity.Color
                if original_color in standard_colors:
                    color_code = f"entity.Color = {original_color}"  # Use original if it's a standard color
                else:
                    color_code = ""
            else:
                color_code = ""
            
            if hasattr(entity, 'LineType'):
                line_type = entity.LineType
                if line_type in standard_line_types:
                    line_type_code = f"try:\n    entity.LineType = '{standard_line_types[line_type]}'"
                    line_type_scale = entity.LineTypeScale
                    line_type_code += f"\n    entity.LineTypeScale = {line_type_scale}\nexcept:\n    pass"
                else:
                    line_type_code = ""
            else:
                line_type_code = ""

            if entity.EntityName == 'AcDbLine':
                start = entity.StartPoint
                end = entity.EndPoint
                return (f"entity = acad.model.AddLine(APoint({start[0]}, {start[1]}, {start[2]}), "f"APoint({end[0]}, {end[1]}, {end[2]}))\n{color_code}\n{line_type_code}\n")
                # return f"entity = acad.model.AddLine(APoint({start[0]}, {start[1]}, {start[2]}), APoint({end[0]}, {end[1]}, {end[2]}))\n{color_code}\n"
            elif entity.EntityName == 'AcDbCircle':
                center = entity.Center
                radius = entity.Radius
                return f"entity = acad.model.AddCircle(APoint({center[0]}, {center[1]}, {center[2]}), {radius})\n{color_code}\n"
            elif entity.EntityName == 'AcDbText':
                insert = entity.InsertionPoint
                text = entity.TextString
                return f"entity = acad.model.AddText('{text}', APoint({insert[0]}, {insert[1]}, {insert[2]}), {entity.Height})\n{color_code}\n"
            elif entity.EntityName == 'AcDbArc':
                center = entity.Center
                radius = entity.Radius
                start_angle = entity.StartAngle
                end_angle = entity.EndAngle
                return f"entity = acad.model.AddArc(APoint({center[0]}, {center[1]}, {center[2]}), {radius}, {start_angle}, {end_angle})\n{color_code}\n"
            else:
                return f"# Entity type {entity.EntityName} not supported"
        except Exception as e:
            return f"# Error processing entity {entity.EntityName}: {str(e)}"

    def generate(self, output_file_dir:str, output_file_dwg, want_time_line:bool=False) -> None:
        code_lines = []
        max_retries = 15
        retry_delay = 5  # seconds
        for attempt in range(max_retries):
            try:
                if want_time_line:
                    entities = list(self.acad.iter_objects())  # Convert to list to get length
                    for i in tqdm(range(len(entities))):
                        entity = entities[i]
                        code_lines.append(self._generate_entity_code(entity))
                else:
                    for entity in tqdm(self.acad.iter_objects(), desc=f"Attempt {attempt + 1}"):
                        code_lines.append(self._generate_entity_code(entity))
                break
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    print("Max retries reached. Exiting.")
                    raise
        output_code = "\n".join(code_lines)

        self._save_to(output_file_dir, output_code, output_file_dwg)
    
    def _save_to(self, output_file_dir, output_file, output_for_dwg):
        basename = os.path.basename(self.file_path)
        output_file_name = os.path.join(output_file_dir, f"template_bridge.py")
        with open(output_file_name, "w", encoding='utf-8') as f:
            f.write(f"file_path = r'{output_for_dwg}'\n")
            f.write("from pyautocad import Autocad, APoint, aDouble\n\n")
            f.write("acad = Autocad(create_if_not_exists=True)\n")
            f.write("acad.app.Documents.Add()\n")
            f.write("acad.app.Visible = True\n\n")
            f.write(output_file)
            f.write("\ntry:\n")
            f.write("    acad_doc = acad.app.ActiveDocument\n")
            f.write("    acad_doc.SaveAs(file_path)\n")
            f.write("    print(f'Drawing saved successfully at {file_path}')\n")
            f.write("except Exception as e:\n")
            f.write("    print(f'Error saving drawing: {e}')\n")
        
        print("Code generation complete. The code has been saved to n1-bridge.py.")
