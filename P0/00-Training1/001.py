# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:44:41 2021

@author: KPS
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class F(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
        
    def setUI(self):
        self.setGeometry(100,100,300, 300)
        self.setWindowTitle('KPS1')
        self.show()
        
if __name__ =="__main__":
    print(__name__)
    app = QApplication(sys.argv)
    ex=F()
    sys.exit(app.exec())
