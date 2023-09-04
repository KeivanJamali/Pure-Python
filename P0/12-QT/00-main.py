import sys
from PyQt5.QtWidgets import QWidget, QApplication


class F(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(50, 50, 400, 400)
        self.setWindowTitle("test1")
        self.show()


if __name__ == "__main__":
    print(__name__)
    app = QApplication(sys.argv)
    my_app = F()
    sys.exit(app.exec_())
