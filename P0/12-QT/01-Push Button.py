import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit


class My_App(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(700, 100, 400, 600)
        self.setWindowTitle("tset 2")
        self.btn1 = QPushButton("copy", self)
        self.btn1.move(50, 100)
        self.btn1.clicked.connect(self.copy)
        self.le1 = QLineEdit(self)
        self.le2 = QLineEdit(self)
        self.le1.move(200, 25)
        self.le1.resize(100, 20)
        self.le2.resize(100, 20)
        self.le2.move(200, 50)
        self.show()

    def copy(self):
        self.le2.setText(self.le1.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = My_App()
    sys.exit(app.exec_())
