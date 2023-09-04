from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
BoxLayout:
    Slider:
        id: slider
        min: 0
        max: 100
        step: 1
        orientation: 'vertical'
"""))
