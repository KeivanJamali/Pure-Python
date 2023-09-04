from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout


class MyGridlayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text='ur name : '))

        self.askname = TextInput(multiline=False)
        self.add_widget(self.askname)


class MyApp(App):
    def build(self):
        return MyGridlayout()


if __name__ == '__main__':
    MyApp().run()
