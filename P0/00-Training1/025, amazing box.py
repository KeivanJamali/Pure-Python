# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:36:31 2021

@author: KPS
"""

import numpy as np
import numpy.matlib

n = int(input('n? '))
a = np.zeros((n,n))
i = 0
j = n//2
for k in range(1, n**2+1):
    if i < 0:
        i += n
    if j < 0:
        j += n
    if a[i,j] == 0:    
        a[i,j] = int(k)
        i -= 1
        j -= 1
    else:
        i += 2
        j += 1
        if i>=n:
            i -= n
        if j>=n:
            j -= n
        a[i,j] = int(k)
        i -= 1
        j -= 1



print(a)