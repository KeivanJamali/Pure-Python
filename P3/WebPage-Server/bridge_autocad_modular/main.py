from bridge_autocad_modular.template_extractor_V3 import Extract_template
from bridge_autocad_modular.Calculations import Calculate
from bridge_autocad_modular.implement_numbers import implementing_in_code
import os

class run:
    def __init__(self, input_dwg, output_file):
        input_file_dir = input_dwg
        self.output_file_dir = output_file
        output_file_dwg = os.path.join(output_file, "bridge.dwg")
        exctractor = Extract_template(file_name=input_file_dir, time_load=30)
        exctractor.generate(output_file_dir=self.output_file_dir, output_file_dwg=output_file_dwg, want_time_line=False)
    def save_files(self, file):
        calculator = Calculate(file)
        file2 = os.path.join(self.output_file_dir, "template_bridge.py")
        impl = implementing_in_code(data=calculator.data, file_dir=file2)
        temp_file = impl.replace_text_in_file()
        return temp_file