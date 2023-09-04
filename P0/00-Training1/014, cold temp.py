# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:39:24 2021

@author: KPS
"""
import math
def main():
    v = float(input('velocity? '))
    t = float(input('temprechure? '))
    print('w is ', calculate(v, t))
    
    
def calculate(v, t):
    return(33 - (10 * math.sqrt(v) - v + 10.5)*(33 - t)/(21.1))

main()