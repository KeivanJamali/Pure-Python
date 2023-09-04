# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:29:31 2021

@author: KPS
"""

def aval(x):
    a = [2]
    Bool = True
    n = 3
    while Bool:
        d = 0
        for i in range(0,len(a)):
            if n % a[i] == 0:
                break
            else:
                d += 1
        if d == len(a):
            a.append(n)
        n += 2
        if len(a) == x:
            Bool = False
    return a
        
def main():
    n = int(input())
    All_avals = aval(n)
    # print_All(All_avals)
    print_last(All_avals)
    
    
def print_last(a):
    print(a[-1])
    
    
def print_All(a):
    for i in a:
        print(i)


main()