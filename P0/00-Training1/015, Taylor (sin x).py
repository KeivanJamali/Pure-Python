# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:53:00 2021

@author: KPS
"""

def fac(n):
    a = 1
    for i in range(1, n+1):
        a = a * i
    return a


def pow(x, n):
    a = 1
    for i in range(n):
        a = a * x
    return a
        
def main():
    x = float(input('sin '))
    n = int(input('how many times? '))
    a = 0
    sng = 1
    for i in range(1, n+1, 2):
        a += pow(x ,i) / fac(i) * sng
        sng = -sng
    print('sin(',x,') is', a)
    
main()