# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:43:55 2021

@author: KPS
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class F(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()
        
    
    def setUI(self):
        self.setGeometry(100, 100, 350, 500)
        self.setWindowTitle('KPS4')
        btn1 = QPushButton('click', self)
        btn1.move(50, 100)
        btn1.clicked.connect(self.click)
        btn2= QPushButton('MSG', self)
        btn2.move(100, 150)
        btn2.clicked.connect(self.MSG)
        self.statusBar().showMessage('Nothing is here')
        self.show()
        
    def click(self):
        self.close()
    def MSG(self):
        qms = QMessageBox.question(self,'Warning',
                                   'do you want to close it?',
                                   QMessageBox.Yes |QMessageBox.No | QMessageBox.Help)
        if qms == QMessageBox.Yes:
            self.close()
        elif qms == QMessageBox.No:
            pass
        elif qms == QMessageBox.Help:
            print('سرکاری')
            
if __name__ =='__main__':
    print(__name__)
    app = QApplication(sys.argv)
    ex=F()
    sys.exit(app.exec())