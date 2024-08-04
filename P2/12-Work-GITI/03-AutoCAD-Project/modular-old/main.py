from template_extractor_V3 import Extract_template
from Calculations import Calculate
from implement_numbers import implementing_in_code

input_file_dir = r"D:\All Python\Pure-Python\P2\12-Work-GITI\03-AutoCAD-Project\Templates\1_bridge.dwg"
output_file_dir = r"D:\All Python\Pure-Python\P2\12-Work-GITI\03-AutoCAD-Project\modular\templates"
output_file_dwg = r"D:\All Python\Pure-Python\P2\12-Work-GITI\03-AutoCAD-Project\dwg\bridge_one.dwg"
exctractor =  Extract_template(file_name=input_file_dir, time_load=30)
exctractor.generate(output_file_dir=output_file_dir, output_file_dwg=output_file_dwg, want_time_line=True)
calculator = Calculate()
file = r"D:\All Python\Pure-Python\P2\12-Work-GITI\03-AutoCAD-Project\modular\templates\template_1_bridge.py"
impl = implementing_in_code(data=calculator.data, file_dir=file)
impl.replace_text_in_file()