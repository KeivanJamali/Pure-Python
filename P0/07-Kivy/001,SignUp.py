from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class SingUp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spacing = 20
        self.orientation = 'vertical'
        self.dic = {}

        self.clearbtn = Button(
            text='clear',
            background_color="#00EAFF",
            color="#FFFFFF",
            font_size=30,
            on_press=self.cleartext
        )

        self.okbtn = Button(
            text='SingUp',
            background_color="#00EAFF",
            color="#FFFFFF",
            font_size=30,
            on_press=self.SingCheck
        )

        self.namebtn = Button(
            text='name',
            background_color="#00EAFF",
            color="#FFFFFF",
            font_size=30,
            on_press=self.nameing
        )

        self.username = TextInput(
            hint_text="Username or Email",
            font_size=30
        )

        self.password = TextInput(
            hint_text="Password",
            font_size=30
        )

        self.pop = Popup(
            title="Error",
            size_hint = (0.5,0.5),
            content=Label(text='')
        )

        self.add_widget(self.username)
        self.add_widget(self.password)
        self.add_widget(self.okbtn)
        self.add_widget(self.clearbtn)
        self.add_widget(self.namebtn)

    def cleartext(self, temp):
        self.username.text = ''
        self.password.text = ''

    def SingCheck(self, temp):
        Bool = 0
        for keys, values in self.dic.items():
            if self.username.text == keys and self.password.text == values:
                self.pop.content.text ='SingUp Successfully!'
                Bool = 1
        if Bool == 0:
            self.pop.content.text="wrong!"
        self.pop.open()
        self.cleartext(Bool)

    def nameing(self, temp):
        Bool = 0
        if len(self.username.text) < 5:
            self.pop.content.text = "please fill the username, it should at lease contain 4 characters."
            Bool = 1
        if len(self.password.text) < 5 and Bool == 0:
            self.pop.content.text = "please fill the password, it should at lease contain 6 characters."
            Bool = 1
        if Bool == 0:
            self.dic[self.username.text] = self.password.text
            print(self.dic)
            self.pop.content.text = "successful!"
        self.pop.open()
        self.cleartext(Bool)


class MyApp(App):
    def build(self):
        return SingUp()


MyApp().run()