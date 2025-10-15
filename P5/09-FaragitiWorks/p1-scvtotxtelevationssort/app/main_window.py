import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QComboBox, QSpinBox, QDoubleSpinBox, QTextEdit, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from main import DataLoader, Engine

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Elevation Data Processor")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QtGui.QIcon(str(Path(__file__).parent / "logo-white.ico")))
        self.data_loader = None
        self.engine = Engine()
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.file_label = QLabel("No file selected.")
        layout.addWidget(self.file_label)

        self.select_file_btn = QPushButton("Select CSV File")
        self.select_file_btn.clicked.connect(self.select_file)
        layout.addWidget(self.select_file_btn)

        self.time_threshold_spin = QDoubleSpinBox()
        self.time_threshold_spin.setValue(0.75)
        self.time_threshold_spin.setMinimum(0.01)
        self.time_threshold_spin.setMaximum(60)
        self.time_threshold_spin.setSingleStep(0.1)
        layout.addWidget(QLabel("Time Threshold (minutes):"))
        layout.addWidget(self.time_threshold_spin)

        self.elevation_threshold_spin = QDoubleSpinBox()
        self.elevation_threshold_spin.setValue(0.0)
        self.elevation_threshold_spin.setMinimum(0.0)
        self.elevation_threshold_spin.setMaximum(100000)
        self.elevation_threshold_spin.setSingleStep(0.1)
        layout.addWidget(QLabel("Elevation Threshold (optional):"))
        layout.addWidget(self.elevation_threshold_spin)

        self.load_btn = QPushButton("Load and Process Data")
        self.load_btn.clicked.connect(self.load_data)
        layout.addWidget(self.load_btn)

        self.group_combo = QComboBox()
        self.group_combo.currentIndexChanged.connect(self.update_group_info)
        layout.addWidget(QLabel("Select Group:"))
        layout.addWidget(self.group_combo)

        self.plot_btn = QPushButton("Plot Selected Group")
        self.plot_btn.clicked.connect(self.plot_group)
        layout.addWidget(self.plot_btn)

        self.save_btn = QPushButton("Save Processed Data")
        self.save_btn.clicked.connect(self.save_data)
        layout.addWidget(self.save_btn)

        self.info_text = QTextEdit()
        self.info_text.setReadOnly(True)
        layout.addWidget(self.info_text)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)")
        if file_path:
            self.file_label.setText(file_path)

    def load_data(self):
        file_path = self.file_label.text()
        if not Path(file_path).exists():
            QMessageBox.warning(self, "Error", "Please select a valid CSV file.")
            return
        time_threshold = self.time_threshold_spin.value()
        elevation_threshold = self.elevation_threshold_spin.value()
        if elevation_threshold == 0.0:
            elevation_threshold = None
        try:
            self.data_loader = DataLoader(filepath=file_path, time_threshold=time_threshold, elevation_threshold=elevation_threshold)
            self.group_combo.clear()
            for i in range(len(self.data_loader.group_data)):
                self.group_combo.addItem(f"Group {i+1}")
            self.info_text.setText(f"Loaded file: {file_path}\nGroups found: {len(self.data_loader.group_data)}\nRemoved notes: {self.data_loader.removed_notes}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def update_group_info(self):
        idx = self.group_combo.currentIndex()
        if self.data_loader and idx >= 0:
            group = self.data_loader.group_data[idx]
            self.info_text.setText(f"Group {idx+1} info:\nRows: {len(group)}\nColumns: {list(group.columns)}")

    def plot_group(self):
        idx = self.group_combo.currentIndex()
        if self.data_loader and idx >= 0:
            group = self.data_loader.group_data[idx].copy()
            self.engine.plot_data(group, idx+1)

    def save_data(self):
        if not self.data_loader:
            QMessageBox.warning(self, "Error", "No data loaded.")
            return
        output_dir = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if output_dir:
            self.data_loader.store_data(output_dir)
            QMessageBox.information(self, "Saved", f"Processed data saved to {output_dir}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
