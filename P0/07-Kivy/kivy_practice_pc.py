import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGridlaout(GridLayout):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        #set columns
        self.cols = 2
        #add widgets
        self.ask_name = TextInput(multiline=False)

        self.add_widget(Label(text='ur name : '), self.ask_name)
        # add input box
        



class MyApp(App):
    def bulid(self):
        return MyGridlaout()


if __name__ == '__main__':
    MyApp().run()
        
















