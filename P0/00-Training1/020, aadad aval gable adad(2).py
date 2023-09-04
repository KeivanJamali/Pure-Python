# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:16:58 2021

@author: KPS
"""

num = int(input('Enter n: '))
a = []
temp = 0
for i in range(2, num+1):
    for t in range(2, i):
        temp = 0
        if  i % t == 0:
            temp += 1
            break
    if temp == 0:
        a.append(i)
        
print(a)