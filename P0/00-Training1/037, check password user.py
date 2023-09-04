# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:48:54 2021

@author: KPS
"""

class User:
    
    def __init__(self):
        self.name = 'fanavarienovin'
        self.Id = 1234
        
    
name = input()
Id = int(input())
if name == User().name and Id == User().Id:
    print('corroct')
else:
    raise SyntaxError('khkhkh')
          
    
    