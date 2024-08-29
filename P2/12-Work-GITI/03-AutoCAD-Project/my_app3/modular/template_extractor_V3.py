from pyautocad import Autocad
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
    def __init__(self, file_name, time_load=30, progress_callback=None) -> None:
        self._progress_callback = progress_callback
        self._intialize_autocad()
        self._open_autocad_file(file_name)
        print("[INFO] AutoCad oppened properly. ---template_extractor_V3 - line 30---")
        self._progress_bar(5)
        time.sleep(time_load)
        self._progress_bar(25)

    def _intialize_autocad(self) -> None:
        """This function will initiate autocad and open it.
        """
        pythoncom.CoInitialize()
        self.acad = Autocad(create_if_not_exists=True)
        self.acad.app.Visible = True

    def _open_autocad_file(self, file_name:str) -> None:
        """This function will open a file.

        Args:
            file_name (str): The dwg file address.
        """
        self.file_path = file_name
        self.acad.app.documents.Open(self.file_path)

    def _progress_bar(self, perc:int) -> None:
        """this function will move the progress bar input further.

        Args:
            perc (int): The percent we are at.
        """
        if self._progress_callback:
            self._progress_callback(perc)

    def _generate_entity_code(self, entity):
        """This code will write down the necessary code for drawing in autocad.

        Args:
            entity (Autocad object): The autocad object that is detected in dwg file.
        """
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
            return f"[ERROR] Couldn't read template. There are some problem in the dwg file. --- template_extractor_V3 - line 93---"

    def generate(self, save_to_file:str, culvert_final_dwg:str, culvert_dwg:str) -> None:
        """This function will generate the py file that will draw exactly like the dwg file.

        Args:
            save_to_file (str): The folder that contains the py file and other files.
            culvert_final_dwg (str): The result file that will save the data on.
            culvert_dwg (str): The empty file that only is needed but not important what is drawn in that file.

        Returns:
            _type_: _description_
        """
        code_lines = []
        max_retries = 15
        retry_delay = 5  # seconds
        for attempt in range(max_retries):
            try:
                # Iterate over entities directly
                model_space = self.acad.doc.ModelSpace
                for entity in model_space:
                    code_lines.append(self._generate_entity_code(entity))
                break
            except Exception as e:
                print(f"[INFO] Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    print(f"[INFO] Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    print("[INFO] Max retries reached. Exiting.")
                    return f"[ERROR] Couldn't read the template. Please open Autocad and try again. --- template_extractor_V3 - line 113---"
        output_code = "\n".join(code_lines)
        self._progress_bar(30)
        self._save_to(save_to_file, output_code, culvert_final_dwg, culvert_dwg)
        self._progress_bar(35)
    
    def _save_to(self, save_to_file:str, output_code:str, culvert_final_dwg:str, culvert_dwg:str):
        """This function will store the file that contains all the necessary code to draw the dwg file.

        Args:
            save_to_file (str): The folder that contains all files.
            output_code (str): All the code that is wrote before for being in this file.
            culvert_final_dwg (str): The resultant file that will be the objective.
            culvert_dwg (str): The temprary file. not important what is in this file. only it should be there.
        """
        output_file_name = os.path.join(save_to_file, f"template_culvert.py")
        with open(output_file_name, "w", encoding='utf-8') as f:
            f.write(f"file_path = r'{culvert_final_dwg}'\n")
            f.write(f"file_to_open = r'{culvert_dwg}'\n")
            f.write("from pyautocad import Autocad, APoint, aDouble\n")
            f.write("import time\n\n")
            f.write("acad = Autocad(create_if_not_exists=True)\n")
            f.write("acad.app.Visible = True\n")
            f.write("acad.app.documents.Open(file_to_open)\n")
            f.write("time.sleep(5)\n")
            f.write("for entity in acad.doc.ModelSpace:\n")
            f.write("    try:\n")
            f.write("        entity.Delete()\n")
            f.write("    except Exception as e:\n")
            f.write("        print(f'[ERROR] Failed to delete entity. ---Try Again---')\n\n")
            f.write(output_code)
            f.write("\ntry:\n")
            f.write("    acad_doc = acad.app.ActiveDocument\n")
            f.write("    acad_doc.SaveAs(file_path)\n")
            f.write("    print(f'[INFO] Drawing saved successfully at {file_path}')\n")
            f.write("except Exception as e:\n")
            f.write("    print(f'[Error] Failed saving drawing: {e}')\n")
        
        print("[INFO] Code generation complete. The code has been saved to template_culvert.py. ---template_extractor_V3 - Done---")
