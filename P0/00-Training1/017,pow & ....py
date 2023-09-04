# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:53:40 2021

@author: KPS
"""

def Pow(a, n):
    if n == 0:
        return 1
    elif n>=1:
        return a * Pow(a, n-1)
    

# def Pow(a, n):
#     b = 1
#     if n == 0:
#         return 1
#     elif n >= 1:
#         for i in n:
#             b = a* b
#             return(b)
        
        
def main():
    for n in range(1000, 10000):
        n1 = n % 10
        temp = n // 10
        n2 = temp % 10
        temp //= 10
        n3 = temp % 10
        temp //= 10
        n4 = temp % 10
        if Pow(n3, 3) + Pow(n2, 2) == Pow(n1, 1) + Pow(n4, 4):
            print(n)
            
main()