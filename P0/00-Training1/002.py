# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 00:30:42 2021

@author: KPS
"""

import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton

class D(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
        
        
    def setUI(self):
        self.setGeometry(100,100,350,350)
        self.setWindowTitle('KPS2')
        btn = QPushButton('close',self)
        btn.move(50,50)
        #btn.clicked.connect(self.p)
        #btn.clicked.connect(self.k)
        btn.clicked.connect(self.exit)
        self.show()
    
    def p(self):
        print('intresting!')
    def k(self):
        print('I know!')
    def exit(self):
        self.close()
        
        
if __name__ == '__main__':
    print(__name__)
    app = QApplication(sys.argv)
    ex = D()
    sys.exit(app.exec())