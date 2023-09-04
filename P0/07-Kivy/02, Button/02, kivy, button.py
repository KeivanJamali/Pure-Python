# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:37:33 2021

@author: KPS
"""

# from kivy.lang import Builder
# from kivy.base import runTouchApp

# runTouchApp(Builder.load_file("kiy.kv"))


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class Myapp(App):
    def build(self):
        f1 = FloatLayout()
        btn = Button(text = "Big one", size_hint = (.2,.2),
                     pos_hint = {'x':.0,'y':.0}, background_color =('yellow'))
        f1.add_widget(btn)
        return f1
    
if __name__ == '__main__':
    Myapp().run()