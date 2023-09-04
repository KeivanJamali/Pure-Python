# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 13:08:27 2021

@author: KPS
"""

def calculate():
    
    """counting smalest moshtarak mazrab"""
    
    a = int(input('first? '))
    b = int(input('seccond? '))
    z = 1
    while(True):
        if z % a == 0 and z % b == 0:
            print(z)
            break
        else:
            z += 1
            
calculate()