# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:06:21 2021

@author: KPS
"""

import math
class Circle:
    r = 0
        
    def __init__(self, r):
        self.r = r
        
    def __del__(self):
        print("object deleted.")
        
    def Area(self):
        return self.r * self.r * math.pi
    
    def prime(self):
        return 2 * math.pi * self.r
    
    def __str__(self):
        s = "R : " + str(self.r)
        s += "\t\tArea : " + str(self.Area())
        s += "\t\tprime : " + str(self.prime())
        return s
    
r = int(input())
c1 = Circle(0)
print(c1)
c2 = Circle(r)
print(c2)
del c1