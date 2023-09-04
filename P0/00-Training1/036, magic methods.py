# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:06:46 2021

@author: KPS
"""

class Person:
    def __init__(self, name):
        
        self.name = name
        
        
    def __repr__(self):
        "what print() will do!"
        return f"person is ({self.name})"
        # return "person is ({})".format(self.name)
    
    
    def __mul__(self, x):
        "what [object * x] can do!"
        if type(x) is not int:
            raise Exception("invalid")
        self.name = self.name * x
    
    
    def __call__(self, y):
        "what object's () can do!"
        print(f'hehehe{y}')
        
        
    def __len__(self):
        "what len(object) do!"
        return len(self.name)
    
    
    def __add__(self, x):
        self.name = self.name + '+' + str(x)
        return self.name
        
        
    def __sub__(self, x):
        self.name = self.name + '-' + str(x)
        return self.name
        
    
    def __del__(self):
        print('bye object!')
        
        
p = Person("ali")
# p * 4
# print(p)
# p(4)
print(p-2, p + 3)