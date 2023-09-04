# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 08:20:50 2021

@author: KPS
"""

from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.lang import Builder


class Pages(PageLayout):
    Builder.load_file("C.kv")
    
    
class MyApp(App):
    def build(self):
        return Pages()
    
    
MyApp().run()