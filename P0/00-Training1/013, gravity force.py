# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:13:48 2021

@author: KPS
"""

def read_wirte():
    m1 = float(input('first? '))
    m2 = float(input('seccond? '))
    d = float(input('distance? '))
    print(calculate(m1, m2, d), 'N')

def calculate(m1 : float, m2 : float, d : float) -> float :
    return(6.693 * 10**-8 * m1 * m2 / d**2)
    
read_wirte()