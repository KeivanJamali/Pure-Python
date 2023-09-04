# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:27:45 2021

@author: KPS
"""

def prim(a, tedad, num):
    for i in range(0, tedad):
        if num%a[i] == 0:
            return 0
    a.append(num)
    return 1
    

def main():
    tedad = 0
    p = []
    n = int(input('Enter n: '))
    for i in range(2, n + 1):
        if prim(p , tedad, i) == 1:
            tedad += 1
    print('primary is', end = '')
    for i in range(0, tedad):
        print(' ',p[i],end='')
            
            
main()