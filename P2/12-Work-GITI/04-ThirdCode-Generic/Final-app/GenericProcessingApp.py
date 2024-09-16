import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog,
                             QMessageBox, QProgressBar, QHBoxLayout, QLineEdit, QFormLayout)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
import os
from modular.Generic_DataLoader_V4 import Generic_DataLoader

class FileProcessor(QThread):
    progress_signal = pyqtSignal(int)
    error_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()

    def __init__(self, input_file=None, epsilon=None, roundlim=None, output_dir=None, progress_callback=None):
        super().__init__()
        self.input_file = input_file
        self.epsilon = epsilon
        self.roundlim = roundlim
        self.output_dir = output_dir
        self.progress_callback = progress_callback                                                            

    def run(self):
        try:
            dataloader = Generic_DataLoader(file_name=self.input_file, progress_callback=self.progress_callback)
            print("[INFO] Dataloader generated.")
            dataloader.fit(epsilon=self.epsilon, round_lim=self.roundlim)
            print("[INFO] Parameters fitted.")
            dataloader.save_files(self.output_dir)
            print("[INFO] Saved. Done!")
            self.finished_signal.emit()
            self.progress_callback(100)
        except Exception as e:
            m = "Something went wrong!"
            self.error_signal.emit(str(e))

    def report_progress(self, progress):
        self.progress_signal.emit(progress)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.password = "Faragiti2552"
        self.setWindowTitle("Generic Processing App")
        self.setGeometry(100, 100, 1000, 600)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.main_page = self.create_main_page()
        self.generate_file_page_csv = self.create_generate_file_page_csv()

        self.layout.addWidget(self.main_page)
        self.layout.addWidget(self.generate_file_page_csv)

        self.timer = QTimer()  # Timer to track elapsed time
        self.timer.timeout.connect(self.update_timer)
        self.seconds_elapsed = 0

        self.show_page(self.main_page)

    def show_page(self, page):
        self.main_page.hide()
        self.generate_file_page_csv.hide()
        page.show()

    def create_main_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        title_label = QLabel("Generic Processing App", page)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; color: black;")
        layout.addWidget(title_label)

        enter_data_button = QPushButton("Enter data", page)
        enter_data_button.clicked.connect(self.proceed_to_method)
        layout.addWidget(enter_data_button)

        info_button = QPushButton("Info", page)
        info_button.clicked.connect(self.show_info)
        layout.addWidget(info_button)

        return page

    def proceed_to_method(self):
        self.show_page(self.generate_file_page_csv)

    def create_generate_file_page_csv(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        size = 30
        # Back button
        self.back_button_csv = QPushButton("Back", page)
        self.back_button_csv.clicked.connect(lambda: self.show_page(self.main_page))
        self.back_button_csv.setFixedHeight(size)  # Set consistent height
        layout.addWidget(self.back_button_csv)

        # CSV Selection (QHBoxLayout for status and button)
        csv_layout = QHBoxLayout()
        self.csv_status = QLabel("CSV: Not Selected", page)
        self.csv_button = QPushButton("Select CSV File", page)
        self.csv_button.clicked.connect(self.select_csv_file)
        self.csv_button.setFixedHeight(size)
        csv_layout.addWidget(self.csv_status)
        csv_layout.addWidget(self.csv_button)
        layout.addLayout(csv_layout)

        # Output directory selection (QHBoxLayout)
        select_layout = QHBoxLayout()
        self.output_status = QLabel("Output directory: Not Selected", page)
        self.output_button = QPushButton("Select output directory", page)
        self.output_button.clicked.connect(self.select_output_dir)
        self.output_button.setFixedHeight(size)
        select_layout.addWidget(self.output_status)
        select_layout.addWidget(self.output_button)
        layout.addLayout(select_layout)

        # Form layout for inputs (Epsilon, Rounding Limit, Password)
        form_layout = QFormLayout()

        self.epsilon = QLineEdit(page)
        self.epsilon.setFixedHeight(size)
        form_layout.addRow(QLabel("Epsilon(m): To cluster and find the ax points.", page), self.epsilon)

        self.roundlim = QLineEdit(page)
        self.roundlim.setFixedHeight(size)
        form_layout.addRow(QLabel("Rounding Limit (m): To round the digits of ax.", page), self.roundlim)

        self.password_in = QLineEdit(page)
        self.password_in.setFixedHeight(size)
        form_layout.addRow(QLabel("Password:", page), self.password_in)

        layout.addLayout(form_layout)

        # Process button
        self.process_button_csv = QPushButton("Process", page)
        self.process_button_csv.clicked.connect(self.start_processing_generate_file_csv)
        self.process_button_csv.setFixedHeight(size)
        layout.addWidget(self.process_button_csv)

        # Progress bar
        self.progress_bar_csv = QProgressBar(page)
        layout.addWidget(self.progress_bar_csv)
        
        # Timer
        self.timer_label = QLabel("Time elapsed: 0 sec", page)
        layout.addWidget(self.timer_label)

        return page


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

    def start_processing_generate_file_csv(self):
        self.seconds_elapsed = 0  # Reset timer
        self.timer.start(1000)  # Start timer, update every second

        self.process_button_csv.setEnabled(False)  # Disable the process button
        self.back_button_csv.setEnabled(False)  # Disable the back button
        self.csv_button.setEnabled(False)  # Disable the DWG button
        self.output_button.setEnabled(False)  # Disable the output directory button
        self.epsilon.setEnabled(False)
        self.roundlim.setEnabled(False)
        self.password_in.setEnabled(False)
        if not hasattr(self, 'csv_file') or not hasattr(self, 'output_dir') or not self.epsilon.text() or not self.roundlim.text():
            QMessageBox.warning(self, "Missing Information", "Please select all required files and directories.")
            self.enable_buttons_csv()
            return
        if not self.password == self.password_in.text():
            QMessageBox.warning(self, "Wrong Password", "Please contact me in my website for password, KeivanJamali.com")
            self.enable_buttons_csv()
            return
        self.process_button_csv.setEnabled(False)
        self.processor = FileProcessor(input_file=self.csv_file, epsilon=float(self.epsilon.text()), roundlim=float(self.roundlim.text()), output_dir=self.output_dir, progress_callback=self.update_progress_csv)
        self.processor.progress_signal.connect(self.update_progress_csv)
        self.processor.error_signal.connect(self.show_error)
        self.processor.finished_signal.connect(self.enable_buttons_csv)
        self.processor.start()

    def enable_buttons_csv(self):
        self.timer.stop()  # Stop the timer when the process is finished
        self.display_elapsed_time()  # Display the elapsed time
        self.process_button_csv.setEnabled(True)
        self.back_button_csv.setEnabled(True)
        self.csv_button.setEnabled(True)
        self.output_button.setEnabled(True)
        self.epsilon.setEnabled(True)
        self.roundlim.setEnabled(True)
        self.password_in.setEnabled(True)
        self.progress_bar_csv.setValue(0)

    def update_progress_csv(self, progress):
        self.progress_bar_csv.setValue(progress)

    def update_progress_manual(self, progress):
        self.progress_bar_manual.setValue(progress)

    def update_progress_dwg(self, progress):
        self.progress_bar_dwg.setValue(progress)

    def update_timer(self):
        self.seconds_elapsed += 1
        self.timer_label.setText(f"Time elapsed: {self.seconds_elapsed} sec")

    def display_elapsed_time(self):
        minutes, seconds = divmod(self.seconds_elapsed, 60)
        time_str = f"Elapsed Time: {minutes} min and {seconds} sec"
        self.timer_label.setText(time_str)

    def show_error(self, error_message):
        QMessageBox.critical(self, "Error", error_message)

    def show_info(self):
        QMessageBox.information(self, "Info", "Generic Processing App\nVersion: 4.0\nDeveloped by: KeivanJamali\nWebsite: keivanjamali.com\nCompany: FaraGiti Andishan")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())
