import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                             QVBoxLayout, QWidget, QFileDialog, QMessageBox, 
                             QProgressBar, QHBoxLayout)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import os
import time
from modular.main import exx
from modular.template_extractor_V3 import Extract_template
from modular.Calculations import Calculate
from modular.implement_numbers import implementing_in_code

class FileProcessor(QThread):
    progress_signal = pyqtSignal(float)
    error_signal = pyqtSignal(str)

    def __init__(self, input_dwg, csv_file, output_dir, py_file=None, dwg_output_dir=None, progress_callback=None):
        super().__init__()
        self.input_dwg = input_dwg
        self.csv_file = csv_file
        self.output_dir = output_dir
        self.py_file = py_file
        self.dwg_output_dir = dwg_output_dir
        self.progress_callback = progress_callback                                                            

    def run(self):
        try:
            if self.py_file:
                done = exx(self.py_file, progress_callback=self.report_progress)
            else:
                # builder = run(input_dwg=self.input_dwg, output_file=self.output_dir, progress_callback=self.report_progress)
                exctractor = Extract_template(file_name=self.input_dwg, time_load=30, progress_callback=self.report_progress)
                print("[INFO] File corrctly read.")
                output_file_dwg = os.path.join(self.output_dir, "bridge.dwg")
                exctractor.generate(output_file_dir=self.output_dir, output_file_dwg=output_file_dwg, want_time_line=False)
                print("[INFO] File correctly generated.")
                calculator = Calculate(self.csv_file, progress_callback=self.progress_callback)
                print("[INFO] Calculation done.")
                m1, m2, m3 = calculator.massage1, calculator.massage2, calculator.massage3
                file2 = os.path.join(self.output_dir, "template_bridge.py")
                impl = implementing_in_code(data=calculator.data, file_dir=file2, progress_callback=self.report_progress)
                temp_file = impl.replace_text_in_file()
                print("[INFO] Finalizing...")
                # massage = builder.save_files(file=self.csv_file)
                # if m1:
                #     massage = m1
                # else:
                #     if m2 and m3:
                #         massage = m2+" / "+m3
                #     elif m2:
                #         massage = m2
                #     elif m3:
                #         massage = m3

                # if massage:
                #     self.error_signal.emit(massage)

        except Exception as e:
            self.error_signal.emit(str(e))

    def report_progress(self, progress):
        self.progress_signal.emit(progress)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoCAD Processing App")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.main_page = self.create_main_page()
        self.generate_file_page = self.create_generate_file_page()
        self.generate_dwg_page = self.create_generate_dwg_page()

        self.layout.addWidget(self.main_page)
        self.layout.addWidget(self.generate_file_page)
        self.layout.addWidget(self.generate_dwg_page)

        self.show_page(self.main_page)

    def show_page(self, page):
        self.main_page.hide()
        self.generate_file_page.hide()
        self.generate_dwg_page.hide()
        page.show()

    def create_main_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        title_label = QLabel("AutoCAD Processing App", page)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; color: black;")
        layout.addWidget(title_label)

        generate_file_button = QPushButton("Generate File", page)
        generate_file_button.clicked.connect(lambda: self.show_page(self.generate_file_page))
        layout.addWidget(generate_file_button)

        generate_dwg_button = QPushButton("Generate DWG", page)
        generate_dwg_button.clicked.connect(lambda: self.show_page(self.generate_dwg_page))
        layout.addWidget(generate_dwg_button)

        info_button = QPushButton("Info", page)
        info_button.clicked.connect(self.show_info)
        layout.addWidget(info_button)

        return page

    def create_generate_file_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        # Back Button
        back_button = QPushButton("Back", page)
        back_button.clicked.connect(lambda: self.show_page(self.main_page))
        layout.addWidget(back_button)
        
        # DWG File Section
        dwg_layout = QHBoxLayout()
        self.dwg_status = QLabel("DWG: Not Selected", page)
        self.dwg_button = QPushButton("Select DWG File", page)
        self.dwg_button.clicked.connect(self.select_dwg_file)
        dwg_layout.addWidget(self.dwg_status)
        dwg_layout.addWidget(self.dwg_button)
        layout.addLayout(dwg_layout)
        
        # CSV File Section
        csv_layout = QHBoxLayout()
        self.csv_status = QLabel("CSV: Not Selected", page)
        self.csv_button = QPushButton("Select CSV File", page)
        self.csv_button.clicked.connect(self.select_csv_file)
        csv_layout.addWidget(self.csv_status)
        csv_layout.addWidget(self.csv_button)
        layout.addLayout(csv_layout)
        
        # Output Directory Section
        output_layout = QHBoxLayout()
        self.output_status = QLabel("Output Directory: Not Selected", page)
        self.output_button = QPushButton("Select Output Directory", page)
        self.output_button.clicked.connect(self.select_output_dir)
        output_layout.addWidget(self.output_status)
        output_layout.addWidget(self.output_button)
        layout.addLayout(output_layout)
        
        # Process Button
        self.process_button = QPushButton("Process", page)
        self.process_button.clicked.connect(self.start_processing_generate_file)
        layout.addWidget(self.process_button)
        
        # Progress Bar
        self.progress_bar = QProgressBar(page)
        layout.addWidget(self.progress_bar)
        
        # Time Label
        self.time_label = QLabel("", page)
        layout.addWidget(self.time_label)
        
        return page

    def create_generate_dwg_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        # Back Button
        back_button = QPushButton("Back", page)
        back_button.clicked.connect(lambda: self.show_page(self.main_page))
        layout.addWidget(back_button)
        
        # PY File Section
        py_layout = QHBoxLayout()
        self.py_status = QLabel("PY File: Not Selected", page)
        self.py_button = QPushButton("Select PY File", page)
        self.py_button.clicked.connect(self.select_py_file)
        py_layout.addWidget(self.py_status)
        py_layout.addWidget(self.py_button)
        layout.addLayout(py_layout)
        
        # DWG Output Directory Section
        dwg_output_layout = QHBoxLayout()
        self.dwg_output_status = QLabel("DWG Output Directory: Not Selected", page)
        self.dwg_output_button = QPushButton("Select Output Directory", page)
        self.dwg_output_button.clicked.connect(self.select_dwg_output_dir)
        dwg_output_layout.addWidget(self.dwg_output_status)
        dwg_output_layout.addWidget(self.dwg_output_button)
        layout.addLayout(dwg_output_layout)
        
        # Process Button
        self.process_button_dwg = QPushButton("Process", page)
        self.process_button_dwg.clicked.connect(self.start_processing_generate_dwg)
        layout.addWidget(self.process_button_dwg)
        
        # Progress Bar
        self.progress_bar_dwg = QProgressBar(page)
        layout.addWidget(self.progress_bar_dwg)
        
        # Time Label
        self.time_label_dwg = QLabel("", page)
        layout.addWidget(self.time_label_dwg)
        
        return page

    def select_dwg_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select DWG File", "", "DWG files (*.dwg)", options=options)
        if file:
            self.dwg_file = file
            self.dwg_status.setText(f"DWG: {os.path.basename(file)}")

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
            self.output_status.setText(f"Output Directory: {directory}")

    def select_py_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select PY File", "", "Python files (*.py)", options=options)
        if file:
            self.py_file = file
            self.py_status.setText(f"PY File: {os.path.basename(file)}")

    def select_dwg_output_dir(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Select Output Directory", options=options)
        if directory:
            self.dwg_output_dir = directory
            self.dwg_output_status.setText(f"DWG Output Directory: {directory}")

    def start_processing_generate_file(self):
        if not hasattr(self, 'dwg_file') or not hasattr(self, 'csv_file') or not hasattr(self, 'output_dir'):
            QMessageBox.warning(self, "Missing Information", "Please select all files and directories before processing.")
            return
        # Disable buttons
        self.dwg_button.setDisabled(True)
        self.csv_button.setDisabled(True)
        self.output_button.setDisabled(True)
        self.process_button.setDisabled(True)
        
        self.processor = FileProcessor(self.dwg_file, self.csv_file, self.output_dir)
        self.processor.progress_signal.connect(self.update_progress_generate_file)
        self.processor.error_signal.connect(self.handle_error)
        self.processor.start()

    def start_processing_generate_dwg(self):
        if not hasattr(self, 'py_file') or not hasattr(self, 'dwg_output_dir'):
            QMessageBox.warning(self, "Missing Information", "Please select all files and directories before processing.")
            return
        # Disable buttons
        self.py_button.setDisabled(True)
        self.dwg_output_button.setDisabled(True)
        self.process_button_dwg.setDisabled(True)
        
        self.processor = FileProcessor(None, None, None, self.py_file, self.dwg_output_dir)
        self.processor.progress_signal.connect(self.update_progress_generate_dwg)
        self.processor.error_signal.connect(self.handle_error)
        self.processor.start()

    def update_progress_generate_file(self, progress):
        self.progress_bar.setValue(int(progress * 100))
        if progress == 1.0:
            # Re-enable buttons
            self.dwg_button.setDisabled(False)
            self.csv_button.setDisabled(False)
            self.output_button.setDisabled(False)
            self.process_button.setDisabled(False)
            QMessageBox.information(self, "Processing Complete", "Files processed and saved successfully.")

    def update_progress_generate_dwg(self, progress):
        self.progress_bar_dwg.setValue(int(progress * 100))
        if progress == 1.0:
            # Re-enable buttons
            self.py_button.setDisabled(False)
            self.dwg_output_button.setDisabled(False)
            self.process_button_dwg.setDisabled(False)
            QMessageBox.information(self, "Processing Complete", "DWG file generated and saved successfully.")

    def handle_error(self, message):
        QMessageBox.critical(self, "ERROR", message)

    def show_info(self):
        QMessageBox.information(self, "Info", "Programmer and designer: Keivan Jamali\nWebsite: keivanjamali.com\nCompany: FaraGiti Andishan")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
