import turtle
import math

wn = turtle.Screen()
Kps = turtle.Turtle()
n = 300


def triangle(x):
    Kps.forward(x / 2)
    Kps.left(135)
    Kps.forward(x / math.sqrt(2) / 2)
    Kps.left(90)
    Kps.forward(x / math.sqrt(2) / 2)
    Kps.left(135)


def triangle2(x):
    Kps.forward(x * 3 / 4)
    Kps.left(135)
    Kps.forward(x / math.sqrt(2))
    Kps.left(90)
    Kps.forward(x / math.sqrt(2) / 2)
    Kps.left(45)
    Kps.forward(x / 4)
    Kps.left(90)


for i in range(4):
    triangle(n)
    triangle2(n)
    Kps.penup()
    Kps.forward(n)
    Kps.left(90)
    Kps.pendown()
wn.mainloop()
