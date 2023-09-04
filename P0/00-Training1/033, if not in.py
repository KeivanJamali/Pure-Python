# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:03:21 2021

@author: KPS
"""

statement = list(input())
rem = (input())
for i in statement:
    if i not in rem:
        print(i, end = '')