# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 08:45:46 2021

@author: KPS
"""

def main():
    stat = list(input())
    ans = ''
    stat = calcu(stat, len(stat))
    for i in range(0, len(stat)):
        ans += stat[i]
    print(ans)
    
def calcu(a, la):
    for i in range(0, la//2):
        temp = a[i]
        a[i] = a[la - 1 - i]
        a[la - 1 - i] = temp
    return a

main()

def new(a):
    return ''.join(reversed((a)))