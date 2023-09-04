# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:55:27 2021

@author: KPS
"""

def main():
    a = []
    n = int(input('Enter N: '))
    for i in range(1,n+1):
        a.append(int(input('Enter Num[' + str(i) + '] : ')))
    if n % 2 == 0:
        m = n//2
        sign = 1
        for i in range(0 ,n):
            sign = -sign
            s = (a[m + i * sign] + a[m - 1 + i * sign])/2
            if  s != 0:
                return(calculate2(s, a, n))
        print('Error, all the Enteris are 0!!!')
    else:
        m = n//2
        sign = 1
        for t in range(0, n):
            sign = -sign
            m = m + t * sign
            if a[m] != 0:
                return(calculate(m, a, n))
        print('Error, all the Enteris are 0!!!')
        
def calculate(m, a, n):
    for i in range(0, n):
        S = a[i]/a[m]
        print(a[i], ' / ', a[m], ' = ', S)
        
        
def calculate2(s, a, n):
    for i in range(0, n):
        S = a[i] / s
        print(a[i], ' / ', s,' = ',S)
        
    
main()