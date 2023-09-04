# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:52:39 2021

@author: KPS
"""

import turtle

kps = turtle.Turtle()
kps.color('#E3AA27','#27E337')

kps.begin_fill()
for i in range(4):
    kps.forward(100)
    kps.left(90)
kps.end_fill()

turtle.done()