# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:17:47 2021

@author: KPS
"""

def main():
    while True:
        tedad = 0
        A = []
        a = int(input())
        for m in range(2, a):
            if prime(A, tedad, m) == 1:
                tedad += 1
        print(check(A, a, tedad))
        if input('continiu? ') != 'yes':
            break
        

def prime(A, n, m):
        for i in range(0, n):
            if m % A[i] == 0:
                return 0
        A.append(m)
        return 1
    
    
def check(A, a, n):
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if A[i] + A[j] == a:
                return [A[i], A[j]]
                
                
main()
                