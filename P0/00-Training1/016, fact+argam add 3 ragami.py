# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:22:25 2021

@author: KPS
"""

def fact(n):
    if n == 0:
        return 1
    elif n >= 1:
        return n *  fact(n-1)
    
    
def main():
    # for s in range(1,10):
    #     S = int(fact(s))
    #     for d in range(1,10):
    #         D = int(fact(d))
    #         for i in range(1,10):
    #             I = int(fact(i))
    #             M = int(S+ D+ I)
    #             s = str(s)
    #             d = str(d)
    #             i = str(i)
    #             num = int(str(s+d+i))
    #             if M == num:
    #                 print(num)
    
    for n in range(100, 1000):
        n1 = n%10
        temp = n//10
        n2 = temp%10
        temp //= 10
        n3 = temp%10
        Sum = fact(n1) + fact(n2) + fact(n3)
        if Sum == n:
            print('the result is ', n)
                    
main()