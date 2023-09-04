from math import *
import sympy as sp


class work:
    def __init__(self, x=0, y=0, T=0, u=0):
        self.x = float(x)
        self.y = float(y)
        self.T = float(T)
        self.u = float(u)
    def give_y(self):
        T = sp.Symbol("T")
        print(sp.solve((T/self.u)*(cosh(self.u*self.x/T)-1)-self.y, T))

    # def give_x(self):

w = work(x=10, y=5, u=15)
w.give_y()
