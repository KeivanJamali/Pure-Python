# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:13:29 2021

@author: KPS
"""

List = []

def Fib(self):
    n1 = 1
    n2 = 1
    Number = int(input('how many numbers do you want me to show? '))
    if Number <= 0:
        return('not supported, try again please.')
    elif Number == 1:
        self.append(1)
        return (self)
    elif Number == 2:
        self.append(1)
        self.append(1)
        return (self)
    else:
        self.append(1)
        self.append(1)
        for n in range(3, Number + 1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            self.append(n3)
        return (self)
    

def Repeat(self):
    if type(self) == str:
        List = []
        sed = Fib(List)
        if type(sed) == list:
            print(sed)
        elif type(sed) == str:
            Repeat(self)
        
Answer = Fib(List)
print(Answer)
B = Repeat(Answer)
if B != None:
    print(B)