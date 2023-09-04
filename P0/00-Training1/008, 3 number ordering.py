# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:20:31 2021

@author: KPS
"""

a = float(input('enter number: '))
b = float(input('enter 2 Number: '))
c = float(input('enter 3 number: '))
if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp
print(a,' ',b,' ',c)