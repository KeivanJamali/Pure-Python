# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:59:35 2021

@author: KPS
"""

def fib (n):
    if n == 1:
        return(1)
    if n == 2:
        return(1)
    return(fib(n-2)+fib(n-1))
def main():
    n = int(input('?'))
    print ('result is: ')
    for i in range(1, n+1):
        print(fib(i), end = '   ')
main()