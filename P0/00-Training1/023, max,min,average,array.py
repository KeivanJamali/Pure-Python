# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:45:23 2021

@author: KPS
"""

import numpy as np
import random
import numpy.matlib

def main():
    n = m = 3
    a = np.matlib.empty((n,m), dtype=(int))
    a = randomm(a, n, m)
    print('sum is ',np.sum(a))
    print('average is ',np.average(a))
    print('max is ',np.amax(a))
    print('min is ',np.amin(a))
    pprint(a,n,m)
    
def randomm(arr, n, m):
    for i in range(0, n):
        for j in range(0, m):
            arr[i, j] = random.randint(0,20)
    return arr


def pprint(arr,n ,m):
    for i in range(0,n):
        for j in range(0,m):
            print(arr[i,j], end = '\t')
        print()


main()
        