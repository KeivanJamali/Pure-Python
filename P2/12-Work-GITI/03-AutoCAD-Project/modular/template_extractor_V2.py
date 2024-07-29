from pyautocad import Autocad, APoint, aDouble
from tqdm.auto import tqdm
import pythoncom
import time

# Initialize the connection to AutoCAD
pythoncom.CoInitialize()
acad = Autocad(create_if_not_exists=True)

# Ensure AutoCAD application is visible
acad.app.Visible = True

# Function to generate code for entities
def generate_entity_code(entity):
    try:
        if hasattr(entity, 'TrueColor'):
            true_color = entity.TrueColor
            color_code = f"entity.TrueColor.SetRGB({true_color.Red}, {true_color.Green}, {true_color.Blue})"
        else:
            color_code = f"entity.Color = {entity.Color}"

        if entity.EntityName == 'AcDbLine':
            start = entity.StartPoint
            end = entity.EndPoint
            return f"entity = acad.model.AddLine(APoint({start[0]}, {start[1]}, {start[2]}), APoint({end[0]}, {end[1]}, {end[2]}))\n{color_code}\n"
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

# Open the drawing
file_path = r"D:\All Python\Pure-Python\P2\12-Work-GITI\03-AutoCAD-Project\Templates\1-bridge.dwg"  # Change this to your file path
acad.app.Documents.Open(file_path)

# Wait for a longer time to ensure the drawing is fully loaded
time.sleep(30)

# Generate code for all entities
code_lines = []

# Retry logic in case of temporary COM errors
max_retries = 15
retry_delay = 15  # seconds

for attempt in tqdm(range(max_retries)):
    try:
        for entity in tqdm(acad.iter_objects()):
            code_lines.append(generate_entity_code(entity))
        break  # If successful, exit the retry loop
    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")
        if attempt < max_retries - 1:
            print(f"Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
        else:
            print("Max retries reached. Exiting.")
            raise

# Save the generated code to a file with UTF-8 encoding
output_code = "\n".join(code_lines)
output_folder = r"D:\All Python\Pure-Python\P2\12-Work-GITI\03-AutoCAD-Project\modular"
with open(f"{output_folder}/n1-bridge.py", "w", encoding='utf-8') as f:
    f.write("from pyautocad import Autocad, APoint, aDouble\n\n")
    f.write("acad = Autocad(create_if_not_exists=True)\n")
    f.write("acad.app.Visible = True\n\n")
    f.write(output_code)

print("Code generation complete. The code has been saved to n1-bridge.py.")
