# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 00:59:45 2021

@author: KPS
"""

import sys
from PyQt5.QtWidgets import QApplication, QPushButton,QMainWindow

class F(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()
        
        
    def setUI(self):
        self.setGeometry(100,100,350,350)
        self.setWindowTitle('KPS3')
        btn = QPushButton('close',self)
        btn.move(60,60)
        btn.clicked.connect(self.close)
        self.statusBar().showMessage('Hey! Hi! Welcome!')
        self.show()
        
        
    def close(self):
        self.close()


if __name__ =='__main__':
    print(__name__)
    app = QApplication(sys.argv)
    ex = F()
    sys.exit(app.exec())