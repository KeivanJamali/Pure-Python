# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:26:57 2021

@author: KPS
"""
n = 0
a = []
def main():
    global n
    n = (int(input('how many student? ')))
    read_array()
    print(select_sort())


def read_array():
    global a
    for i in range(1,n+1):
        # print('Enter Id ', i)
        # b = int(input())
        # print()
        # a.append(b)
        a.append(int(input("Enter Id: [" + str(i + 1) + "] = ")))


def select_sort():
    for i in range(0, n):
        for t in range(0, n):
            if i < t:
                if a[i] > a[t]:
                    temp = a[i]
                    a[i] = a[t]
                    a[t] = temp
    return a

main()
                