# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:01:02 2021

@author: KPS
"""

import math, turtle

wn = turtle.Screen()
wn.bgcolor('#E5D3D3')
kps = turtle.Turtle()
kps.color('#03A8E4', '#E103E4')
kps.speed(10)
for j in range(51):
    kps.forward(math.e*j/2)
    kps.left(12.5)
    if j % 5 == 0:
        kps.begin_fill()
    for i in range(5):
        kps.forward(j*3)
        kps.right(144)
    if j % 5 == 0:
        kps.end_fill()

wn.mainloop()