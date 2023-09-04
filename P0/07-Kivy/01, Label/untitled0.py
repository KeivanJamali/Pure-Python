# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:05:36 2021

@author: KPS
"""

from kivy.app import App
from kivy.lang import Builder

myapp = Builder.load_file('eww.kv')

class Myapp(App):
    def build(self):
        return myapp
    
Myapp().run()