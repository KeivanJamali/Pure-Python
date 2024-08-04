from modular.template_extractor_V3 import Extract_template
from modular.Calculations import Calculate
from modular.implement_numbers import implementing_in_code
import os

class run:
    def __init__(self, input_dwg, output_file, progress_callback=None):
        input_file_dir = input_dwg
        self.output_file_dir = output_file
        output_file_dwg = os.path.join(output_file, "bridge.dwg")
        self.progress_callback = progress_callback

        exctractor = Extract_template(file_name=input_file_dir, time_load=30, progress_callback=progress_callback)
        # if self.progress_callback:
            # self.progress_callback(0.5)
        exctractor.generate(output_file_dir=self.output_file_dir, output_file_dwg=output_file_dwg, want_time_line=True)
        # if self.progress_callback:
            # self.progress_callback(0.75)

    def save_files(self, file):
        calculator = Calculate(file, progress_callback=self.progress_callback)
        m1 = calculator.massage2
        m2 = calculator.massage3
        file2 = os.path.join(self.output_file_dir, "template_bridge.py")
        impl = implementing_in_code(data=calculator.data, file_dir=file2, progress_callback=self.progress_callback)
        temp_file = impl.replace_text_in_file()
        # if self.progress_callback:
        #     self.progress_callback(1.0)
        
        if m1 and m2:
            return m1+" / "+m2
        elif m1:
            return m1
        elif m2:
            return m2
        
class exx:
    def __init__(self, input_file, progress_callback=None):
        with open(input_file, 'r', encoding='utf-8') as file:
            exec(file.read())
        if progress_callback:
            progress_callback(1.0)
