from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 450)
Config.set('graphics', 'height', 600)

from persiantools.jdatetime import JalaliDate
import datetime
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

sh = {"فروردین": 31, "اردیبهشت": 31, "خرداد": 31, "تیر": 31, "مرداد": 31, "شهریور": 31,
      "مهر": 30, "ابان": 30, "اذر": 30, "دی": 30, "بهمن": 30, "اسفند": 29}
mil = {"January": 31, "february": 28, "march": 31, "April": 30, "may": 31, "June": 31,
       "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}


def milad_to_shams(List):
    return JalaliDate.to_jalali(List[0], List[1], List[2])


def shams_to_milad(List):
    return JalaliDate(List[0], List[1], List[2]).to_gregorian()


class Mng(ScreenManager):
    pass


chose_shams = ObjectProperty(None)
chose_milad = ObjectProperty(None)
day = ObjectProperty(None)
month = ObjectProperty(None)
year = ObjectProperty(None)
date_shams = ObjectProperty(None)
date_milad = ObjectProperty(None)
date_gamar = ObjectProperty(None)


class Mainsc(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Shape())
        self.btn_ok = Button(text="OK", pos_hint={"x": 0.3, "y": 0.03}, size_hint=(0.4, 0.1), disabled=True)
        self.add_widget(self.btn_ok)
        self.btn_me = Button(text="Me", size_hint=(0.1, 0.05), on_press=self.MME)
        self.add_widget(self.btn_me)
        ######################################################################################################
        self.btn_1 = Button(text="Shamsi to Miladi", pos_hint={"x": 0.1, "y": 0.88}, size_hint=(0.8, 0.1),
                            on_press=self.S_M)
        self.add_widget(self.btn_1)
        ######################################################################################################
        self.btn_2 = Button(text="Miladi to Shamsi", pos_hint={"x": 0.1, "y": 0.77}, size_hint=(0.8, 0.1),
                            on_press=self.M_S)
        self.add_widget(self.btn_2)
        ######################################################################################################
        ######################################################################################################
        self.lbl_1 = Label(text="0/0/0", size_hint=(0.2, 0.1), pos_hint={"x": 0.5, "y": 0.52})
        self.add_widget(self.lbl_1)
        ######################################################################################################
        self.lbl_2 = Label(text="0/0/0", size_hint=(0.2, 0.1), pos_hint={"x": 0.5, "y": 0.38})
        self.add_widget(self.lbl_2)
        ######################################################################################################
        self.lbl_3 = Label(text="0/0/0", size_hint=(0.2, 0.1), pos_hint={"x": 0.5, "y": 0.23})
        self.add_widget(self.lbl_3)

    # Explain about me
    def MME(self, *args):
        ap.current = "Me"

    # change the current shape of buttons
    def S_M(self, *args):
        self.btn_1.disabled = True
        self.btn_2.disabled = False
        self.btn_ok.disabled = False

    def M_S(self, *arrgs):
        self.btn_1.disabled = False
        self.btn_2.disabled = True
        self.btn_ok.disabled = False


class Shape(Widget):
    pass


class Shapeme(Widget):
    pass


class Mesc(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Shapeme())
        self.btn = Button(text="KPS", pos_hint={"x": 0.2, "y": 0.38}, size_hint=(0.6, 0.3), font_size=60,
                          on_press=self.back)
        self.add_widget(self.btn)

    def back(self, *args):
        ap.transition.direction = "right"
        ap.current = "Main"


ap = Mng()


class Time_converterApp(App):
    def build(self):
        ap.add_widget(Mainsc(name="Main"))
        ap.add_widget((Mesc(name="Me")))
        return ap


Time_converterApp().run()
