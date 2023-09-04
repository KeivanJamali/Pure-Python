# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 20:31:10 2021

@author: KPS
"""

def fact(x):
    if x == 0:
        return 1
    return x*fact(x)

fact(5)