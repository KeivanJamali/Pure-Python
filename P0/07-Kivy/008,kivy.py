from kivy.app import App
from kivy.lang import Builder
from kivy.uix.bubble import Bubble
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class Demo(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.but = Button(text="press", on_release=self.show_bub, size_hint=(None,None),
                          size=(100,100), x=Window.width/2 - 50)
        self.add_widget(self.but)
        self.bub = copy()
    def show_bub(self, instance):
        self.add_widget(self.bub)

class copy(Bubble):
    Builder.load_file("008.kv")

class BubApp(App):
    def build(self):
        return Demo()

BubApp().run()