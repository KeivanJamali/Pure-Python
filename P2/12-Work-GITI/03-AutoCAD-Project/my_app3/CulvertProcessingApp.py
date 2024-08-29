import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog,
                             QMessageBox, QProgressBar, QHBoxLayout, QLineEdit, QRadioButton, QGridLayout)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import os
import pandas as pd
from modular.excute_pyfile import exx
from modular.template_extractor_V3 import Extract_template
from modular.Calculations import Calculate
from modular.implement_numbers import implementing_in_code

class FileProcessor(QThread):
    progress_signal = pyqtSignal(int)
    error_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()

    def __init__(self, input_dwg=None, csv_file=None, output_dir=None, dwg_output_dir=None, progress_callback=None):
        super().__init__()
        self.input_dwg = input_dwg
        self.csv_file = csv_file
        self.output_dir = output_dir
        self.dwg_output_dir = dwg_output_dir
        self.progress_callback = progress_callback                                                            

    def run(self):
        try:
            exctractor = Extract_template(file_name=self.input_dwg, time_load=10, progress_callback=self.report_progress)
            print("[INFO] File correctly read.")
            culvert_final_dwg = os.path.join(self.output_dir, "Culvert-Final.dwg")
            culvert_dwg = os.path.join(self.output_dir, "Culvert.dwg")
            exctractor.generate(save_to_file=self.output_dir, culvert_final_dwg=culvert_final_dwg, culvert_dwg=culvert_dwg)
            print("[INFO] File correctly generated.")
            calculator = Calculate(self.csv_file, progress_callback=self.progress_callback)
            print("[INFO] Calculation done.")
            m = calculator.massage
            file2 = os.path.join(self.output_dir, "template_culvert.py")
            if calculator.data:
                impl = implementing_in_code(data=calculator.data, file_dir=file2, progress_callback=self.report_progress)
                temp_file = impl.replace_text_in_file()
            print("[INFO] Finalizing...")
            done = exx(file2, progress_callback=self.report_progress)
            self.finished_signal.emit()
            if m:
                self.error_signal.emit((str(m)))
            print("[INFO] Finished.")

        except Exception as e:
            self.error_signal.emit(str(e))

    def report_progress(self, progress):
        self.progress_signal.emit(progress)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoCAD Processing App")
        self.setGeometry(100, 100, 1000, 600)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.main_page = self.create_main_page()
        self.generate_file_page_csv = self.create_generate_file_page_csv()
        self.generate_file_page_manual = self.create_generate_file_page_manual()

        self.layout.addWidget(self.main_page)
        self.layout.addWidget(self.generate_file_page_csv)
        self.layout.addWidget(self.generate_file_page_manual)

        self.show_page(self.main_page)

    def show_page(self, page):
        self.main_page.hide()
        self.generate_file_page_csv.hide()
        self.generate_file_page_manual.hide()
        page.show()

    def create_main_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        title_label = QLabel("AutoCAD Culvert Processing App", page)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; color: black;")
        layout.addWidget(title_label)

        method_label = QLabel("Select Method for Generating File:", page)
        layout.addWidget(method_label)

        self.radio_csv = QRadioButton("With CSV File", page)
        self.radio_manual = QRadioButton("Input Parameters in App", page)
        layout.addWidget(self.radio_csv)
        layout.addWidget(self.radio_manual)

        next_button = QPushButton("Next", page)
        next_button.clicked.connect(self.proceed_to_method)
        layout.addWidget(next_button)

        info_button = QPushButton("Info", page)
        info_button.clicked.connect(self.show_info)
        layout.addWidget(info_button)

        return page

    def proceed_to_method(self):
        if self.radio_csv.isChecked():
            self.show_page(self.generate_file_page_csv)
        elif self.radio_manual.isChecked():
            self.show_page(self.generate_file_page_manual)
        else:
            QMessageBox.warning(self, "No Selection", "Please select a method.")

    def create_generate_file_page_csv(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        self.back_button_csv = QPushButton("Back", page)
        self.back_button_csv.clicked.connect(lambda: self.show_page(self.main_page))
        layout.addWidget(self.back_button_csv)
        
        dwg_layout = QHBoxLayout()
        self.dwg_status_csv = QLabel("DWG: Not Selected", page)
        self.dwg_button_csv = QPushButton("Select DWG File", page)
        self.dwg_button_csv.clicked.connect(self.select_dwg_file)
        dwg_layout.addWidget(self.dwg_status_csv)
        dwg_layout.addWidget(self.dwg_button_csv)
        layout.addLayout(dwg_layout)
        
        csv_layout = QHBoxLayout()
        self.csv_status = QLabel("CSV: Not Selected", page)
        self.csv_button_csv = QPushButton("Select CSV File", page)
        self.csv_button_csv.clicked.connect(self.select_csv_file)
        csv_layout.addWidget(self.csv_status)
        csv_layout.addWidget(self.csv_button_csv)
        layout.addLayout(csv_layout)
        
        output_layout = QHBoxLayout()
        self.output_status_csv = QLabel("Output Directory: Not Selected", page)
        self.output_button_csv = QPushButton("Select Output Directory", page)
        self.output_button_csv.clicked.connect(self.select_output_dir)
        output_layout.addWidget(self.output_status_csv)
        output_layout.addWidget(self.output_button_csv)
        layout.addLayout(output_layout)
        
        self.process_button_csv = QPushButton("Process", page)
        self.process_button_csv.clicked.connect(self.start_processing_generate_file_csv)
        layout.addWidget(self.process_button_csv)
        
        self.progress_bar_csv = QProgressBar(page)
        layout.addWidget(self.progress_bar_csv)
        
        return page

    def create_generate_file_page_manual(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        self.back_button_mn = QPushButton("Back", page)
        self.back_button_mn.clicked.connect(lambda: self.show_page(self.main_page))
        layout.addWidget(self.back_button_mn)

        dwg_layout = QHBoxLayout()
        self.dwg_status_mn = QLabel("DWG: Not Selected", page)
        self.dwg_button_mn = QPushButton("Select DWG File", page)
        self.dwg_button_mn.clicked.connect(self.select_dwg_file_mn)
        dwg_layout.addWidget(self.dwg_status_mn)
        dwg_layout.addWidget(self.dwg_button_mn)
        layout.addLayout(dwg_layout)

        output_layout = QHBoxLayout()
        self.output_status_mn = QLabel("Output Directory: Not Selected", page)
        self.output_button_mn = QPushButton("Select Output Directory", page)
        self.output_button_mn.clicked.connect(self.select_output_dir_mn)
        output_layout.addWidget(self.output_status_mn)
        output_layout.addWidget(self.output_button_mn)
        layout.addLayout(output_layout)

        grid_layout = QGridLayout()
        self.input_fields = {}
        # -------------------------------------------------------------------------------------------
        label = QLabel("Number of openings:", page)
        input_field = QLineEdit(page)
        self.input_fields["Number of openings:"] = input_field
        row = (1 - 1) // 5
        col = (1 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Opening length (meters):", page)
        input_field = QLineEdit(page)
        self.input_fields["Opening length (meters):"] = input_field
        row = (2 - 1) // 5
        col = (2 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Culvert length (meters):", page)
        input_field = QLineEdit(page)
        self.input_fields["Culvert length (meters):"] = input_field
        row = (3 - 1) // 5
        col = (3 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("HS (HS):", page)
        input_field = QLineEdit(page)
        self.input_fields["HS (HS):"] = input_field
        row = (4 - 1) // 5
        col = (4 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Minimum support height (meters):", page)
        input_field = QLineEdit(page)
        self.input_fields["Minimum support height (meters):"] = input_field
        row = (5 - 1) // 5
        col = (5 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Project axis:", page)
        input_field = QLineEdit(page)
        self.input_fields["Project axis:"] = input_field
        row = (6 - 1) // 5
        col = (6 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Natural ground axis:", page)
        input_field = QLineEdit(page)
        self.input_fields["Natural ground axis:"] = input_field
        row = (7 - 1) // 5
        col = (7 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Right side DEVER:", page)
        input_field = QLineEdit(page)
        self.input_fields["Right side DEVER:"] = input_field
        row = (8 - 1) // 5
        col = (8 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Left side DEVER:", page)
        input_field = QLineEdit(page)
        self.input_fields["Left side DEVER:"] = input_field
        row = (9 - 1) // 5
        col = (9 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Natural ground slope (e.g., 0.01):", page)
        input_field = QLineEdit(page)
        self.input_fields["Natural ground slope (e.g., 0.01):"] = input_field
        row = (10 - 1) // 5
        col = (10 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Longitudinal slope (e.g., -0.01):", page)
        input_field = QLineEdit(page)
        self.input_fields["Longitudinal slope (e.g., -0.01):"] = input_field
        row = (11 - 1) // 5
        col = (11 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Slope of embankment (e.g., 3):", page)
        input_field = QLineEdit(page)
        self.input_fields["Slope of embankment (e.g., 3):"] = input_field
        row = (12 - 1) // 5
        col = (12 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Ret (meters):", page)
        input_field = QLineEdit(page)
        self.input_fields["Ret (meters):"] = input_field
        row = (13 - 1) // 5
        col = (13 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Support angle (degrees):", page)
        input_field = QLineEdit(page)
        self.input_fields["Support angle (degrees):"] = input_field
        row = (14 - 1) // 5
        col = (14 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Parameter A:", page)
        input_field = QLineEdit(page)
        self.input_fields["Parameter A:"] = input_field
        row = (15 - 1) // 5
        col = (15 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Parameter B:", page)
        input_field = QLineEdit(page)
        self.input_fields["Parameter B:"] = input_field
        row = (16 - 1) // 5
        col = (16 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Upper city", page)
        input_field = QLineEdit(page)
        self.input_fields["Upper city"] = input_field
        row = (17 - 1) // 5
        col = (17 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Lower city", page)
        input_field = QLineEdit(page)
        self.input_fields["Lower city"] = input_field
        row = (18 - 1) // 5
        col = (18 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Is the left in autocad 'upper'? (True, False):", page)
        input_field = QLineEdit(page)
        self.input_fields["Is the left in autocad 'upper'? (True, False):"] = input_field
        row = (19 - 1) // 5
        col = (19 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Project description line 1:", page)
        input_field = QLineEdit(page)
        self.input_fields["Project description line 1:"] = input_field
        row = (20 - 1) // 5
        col = (20 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Project description line 2:", page)
        input_field = QLineEdit(page)
        self.input_fields["Project description line 2:"] = input_field
        row = (21 - 1) // 5
        col = (21 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Project description line 3:", page)
        input_field = QLineEdit(page)
        self.input_fields["Project description line 3:"] = input_field
        row = (22 - 1) // 5
        col = (22 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Map Topic Line 1:", page)
        input_field = QLineEdit(page)
        self.input_fields["Map Topic Line 1:"] = input_field
        row = (23 - 1) // 5
        col = (23 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Map Topic Line 2:", page)
        input_field = QLineEdit(page)
        self.input_fields["Map Topic Line 2:"] = input_field
        row = (24 - 1) // 5
        col = (24 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Map Topic Line 3:", page)
        input_field = QLineEdit(page)
        self.input_fields["Map Topic Line 3:"] = input_field
        row = (25 - 1) // 5
        col = (25 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Map Number:", page)
        input_field = QLineEdit(page)
        self.input_fields["Map Number:"] = input_field
        row = (26 - 1) // 5
        col = (26 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Employer:", page)
        input_field = QLineEdit(page)
        self.input_fields["Employer:"] = input_field
        row = (27 - 1) // 5
        col = (27 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Consultant Engineer:", page)
        input_field = QLineEdit(page)
        self.input_fields["Consultant Engineer:"] = input_field
        row = (28 - 1) // 5
        col = (28 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Contractor:", page)
        input_field = QLineEdit(page)
        self.input_fields["Contractor:"] = input_field
        row = (29 - 1) // 5
        col = (29 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Project Title:", page)
        input_field = QLineEdit(page)
        self.input_fields["Project Title:"] = input_field
        row = (30 - 1) // 5
        col = (30 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Notification Date:", page)
        input_field = QLineEdit(page)
        self.input_fields["Notification Date:"] = input_field
        row = (31 - 1) // 5
        col = (31 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Culvert Span:", page)
        input_field = QLineEdit(page)
        self.input_fields["Culvert Span:"] = input_field
        row = (32 - 1) // 5
        col = (32 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Culvert Location:", page)
        input_field = QLineEdit(page)
        self.input_fields["Culvert Location:"] = input_field
        row = (33 - 1) // 5
        col = (33 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Maximum Soil Height Over Culvert:", page)
        input_field = QLineEdit(page)
        self.input_fields["Maximum Soil Height Over Culvert:"] = input_field
        row = (34 - 1) // 5
        col = (34 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        label = QLabel("Turb Angle:", page)
        input_field = QLineEdit(page)
        self.input_fields["Turb Angle:"] = input_field
        row = (35 - 1) // 5
        col = (35 - 1) % 5
        grid_layout.addWidget(label, row * 2, col)
        grid_layout.addWidget(input_field, row * 2 + 1, col)

        # Adjust the spacing between input fields
        for i in range(len(self.input_fields)):
            if i % 5 == 0:
                grid_layout.setSpacing(10)  # Add spacing before the start of a new row
            grid_layout.setVerticalSpacing(5)
        # -------------------------------------------------------------------------------------------
        self.process_button_manual = QPushButton("Process", page)
        self.process_button_manual.clicked.connect(self.process_manual_input)
        grid_layout.addWidget(self.process_button_manual, 15, 4)

        layout.addLayout(grid_layout)
        self.progress_bar_manual = QProgressBar(page)
        layout.addWidget(self.progress_bar_manual)

        return page

    def select_dwg_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select DWG File", "", "DWG files (*.dwg)", options=options)
        if file:
            self.dwg_file = file
            self.dwg_status_csv.setText(f"DWG: {os.path.basename(file)}")

    def select_dwg_file_mn(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select DWG File", "", "DWG files (*.dwg)", options=options)
        if file:
            self.dwg_file = file
            self.dwg_status_mn.setText(f"DWG: {os.path.basename(file)}")

    def select_csv_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV files (*.csv)", options=options)
        if file:
            self.csv_file = file
            self.csv_status.setText(f"CSV: {os.path.basename(file)}")

    def select_output_dir(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Select Output Directory", options=options)
        if directory:
            self.output_dir = directory
            self.output_status_csv.setText(f"Output Directory: {directory}")

    def select_output_dir_mn(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Select Output Directory", options=options)
        if directory:
            self.output_dir = directory
            self.output_status_mn.setText(f"Output Directory: {directory}")

    def start_processing_generate_file_csv(self):
        self.process_button_csv.setEnabled(False)  # Disable the process button
        self.back_button_csv.setEnabled(False)  # Disable the back button
        self.dwg_button_csv.setEnabled(False)  # Disable the DWG button
        self.csv_button_csv.setEnabled(False)  # Disable the CSV button
        self.output_button_csv.setEnabled(False)  # Disable the output directory button
        if not hasattr(self, 'dwg_file') or not hasattr(self, 'csv_file') or not hasattr(self, 'output_dir'):
            QMessageBox.warning(self, "Missing Information", "Please select all required files and directories.")
            self.enable_buttons_csv()
            return
        self.process_button_csv.setEnabled(False)
        self.processor = FileProcessor(input_dwg=self.dwg_file, csv_file=self.csv_file, output_dir=self.output_dir, progress_callback=self.update_progress_csv)
        self.processor.progress_signal.connect(self.update_progress_csv)
        self.processor.error_signal.connect(self.show_error)
        self.processor.finished_signal.connect(self.enable_buttons_csv)
        self.processor.start()

    def enable_buttons_csv(self):
        self.process_button_csv.setEnabled(True)  # Enable the process button
        self.back_button_csv.setEnabled(True)  # Enable the back button
        self.dwg_button_csv.setEnabled(True)  # Enable the DWG button
        self.csv_button_csv.setEnabled(True)  # Enable the CSV button
        self.output_button_csv.setEnabled(True)  # Enable the output directory button
        self.progress_bar_csv.setValue(0)

    def collect_input_data(self):
        input_data = {}
        for key, input_field in self.input_fields.items():
            value = input_field.text()
            if value == "":
                input_data[key] = ""
            else:
                input_data[key] = value
        return input_data

    def process_manual_input(self):
        parameters = self.collect_input_data()
        data = pd.DataFrame(parameters, index=[0]).T
        data.to_csv("input_form.csv", index=True, header=False)
        print("[INFO] input_form SAVED!")
        absolute_path = os.path.abspath("input_form.csv")
        self.dwg_button_mn.setEnabled(False)
        self.process_button_manual.setEnabled(False)
        self.back_button_mn.setEnabled(False)
        self.output_button_mn.setEnabled(False)
        if not hasattr(self, 'dwg_file') or not hasattr(self, 'output_dir'):
            QMessageBox.warning(self, "Missing Information", "Please select all required files and directories.")
            self.enable_buttons_manual()
            return
        self.processor = FileProcessor(input_dwg=self.dwg_file, csv_file=absolute_path, output_dir=self.output_dir, progress_callback=self.update_progress_manual)
        self.processor.progress_signal.connect(self.update_progress_manual)
        self.processor.error_signal.connect(self.show_error)
        self.processor.finished_signal.connect(self.enable_buttons_manual)
        self.processor.start()

    def enable_buttons_manual(self):
        self.dwg_button_mn.setEnabled(True)  # Enable the process button
        self.process_button_manual.setEnabled(True)  # Enable the back button
        self.back_button_mn.setEnabled(True)  # Enable the DWG button
        self.output_button_mn.setEnabled(True)  # Enable the CSV button
        self.progress_bar_manual.setValue(0)

    def update_progress_csv(self, progress):
        self.progress_bar_csv.setValue(progress)

    def update_progress_manual(self, progress):
        self.progress_bar_manual.setValue(progress)

    def update_progress_dwg(self, progress):
        self.progress_bar_dwg.setValue(progress)

    def show_error(self, error_message):
        QMessageBox.critical(self, "Error", error_message)

    def show_info(self):
        QMessageBox.information(self, "Info", "AutoCAD Processing App\nVersion: 1.0\nDeveloped by: KeivanJamali\nWebsite: keivanjamali.com")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())
