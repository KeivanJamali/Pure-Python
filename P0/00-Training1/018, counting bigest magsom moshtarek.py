# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:50:53 2021

@author: KPS
"""

def calculate():
    
    """counting bigest magsom moshtarek"""
    
    a = int(input('first number? '))
    b = int(input('seccond number? '))
    for n in range(a, 0, -1):
        if a % n == 0:
            for m in range(b, 0, -1):
                if b % m == 0:
                    if n == m:
                        return(n)
                       

print(calculate())