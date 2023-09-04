# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:33:14 2021

@author: KPS
"""

import turtle
kps = turtle.Turtle()

kps.color('red', 'yellow')
kps.speed(10)
kps.begin_fill()
for i in range(50):
    kps.forward(200)
    kps.left(168.5)
kps.end_fill()
kps.goto(-200,100)






turtle.done()