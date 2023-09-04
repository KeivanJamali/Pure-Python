# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 07:58:46 2021

@author: KPS
"""

# from kivy.lang import Builder
# from kivy.base import runTouchApp

# runTouchApp(Builder.load_string("""
# GridLayout:
#     cols: 3
#     spacing: 20
    
#     Button:
#         text: 'Kps'
#     Button:
#         text: 'Paniz'
#     Button:
#         text: 'pouya'
#     Button:
#         text: 'sana'
# """))


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

class Grid(GridLayout):
    Builder.load_file("Grid.kv")
    
    
class MyApp(App):
    def build(self):
        return Grid()
    
    
MyApp().run()