# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:06:45 2021

@author: KPS
"""


def main():
    n = int(input('How many number do you like to write? '))
    convert(input1(n),n)

def input1(n):
    a = []
    for i in range(1,n+1):
        a.append(input('write your ' + str(i) + 'th number please.'))
    return(a)

def convert(arr,n):
    temp = 0
    m = n
    for i in range(0,n):
        if m >= 0:
            for j in range(0,m-1):
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            m -= 1
    print(arr)
    
    
main()