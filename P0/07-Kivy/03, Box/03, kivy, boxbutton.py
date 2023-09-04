# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 07:27:34 2021

@author: KPS
"""

from kivy.lang import Builder
from kivy.app import App
from kivy.base import runTouchApp

# runTouchApp(Builder.load_string("""
# BoxLayout:
    
#     orientation : 'vertical'  #or horizontal
    
#     spacing : 10              #distance between buttons
#     Button:
#         text : 'btn 1'
#     Button:
#         text : 'btn 2'
#     Button:
#         text : 'btn 3'
# """

from kivy.uix.boxlayout import BoxLayout

class Kvbl(BoxLayout):
    Builder.load_file('A.kv')
    
    
class MyApp(App):
    def build(self):
        return Kvbl()
    
MyApp().run()