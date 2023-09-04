from kivy.config import Config

Config.set('graphics', 'resizable', 0)

import statistics, math
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen


class Pop_Er(Popup):
    """
    show invalid in the first page.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lb = Button(text="", on_press=self.close)
        self.add_widget(self.lb)
        self.size_hint = (0.6, 0.4)

    def close(self, *args):
        self.dismiss()


class Win2(GridLayout):
    """
    result page view: 9 buttons
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 5
        self.spacing = 1
        # ----------------------------------------------------------------------------------------------------
        self.lb1 = Button(text="average", background_color="yellow", disabled=True, color="black")
        self.lb1r = Button(text="", background_color="yellow", disabled=True, color="black")
        self.lb2 = Button(text="variance", background_color="green", disabled=True, color="black")
        self.lb2r = Button(text="", background_color="green", disabled=True, color="black")
        self.lb3 = Button(text="standard deviation", background_color="yellow", disabled=True, color="black")
        self.lb3r = Button(text="", background_color="yellow", disabled=True, color="black")
        self.lb4 = Button(text="average standard deviation", background_color="green", disabled=True, color="black")
        self.lb4r = Button(text="", background_color="green", disabled=True, color="black")
        self.btnn = Button(text="show new results", background_color="#00FFF9", on_press=self.calculate, color="black")
        self.btn = Button(text="back", background_color="#00FFF9", on_press=ResultScreen.switch_R_to_M, color="black")
        # ----------------------------------------------------------------------------------------------------
        self.add_widget(self.lb1)
        self.add_widget(self.lb1r)
        self.add_widget(self.lb2)
        self.add_widget(self.lb2r)
        self.add_widget(self.lb3)
        self.add_widget(self.lb3r)
        self.add_widget(self.lb4)
        self.add_widget(self.lb4r)
        self.add_widget(self.btn)
        self.add_widget(self.btnn)

    def calculate(self, *args):
        self.lb1r.text = str(sum(data) / len(data))
        if bool(d) == True:
            self.lb2r.text = str(statistics.variance(data))
            x = statistics.stdev(data)
            self.lb3r.text = str(x)
            self.lb4r.text = str(x / math.sqrt(len(data)))
        elif bool(d) == False:
            x = statistics.pvariance(data)
            self.lb2r.text = str(x)
            self.lb3r.text = str(math.sqrt(x))
            self.lb4r.text = str(math.sqrt(x) / math.sqrt(len(data)))


class Win(FloatLayout):
    """
    main page view: 5 buttons and 1 textinput
    """
    global data, d
    data = []
    d = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ----------------------------------------------------------------------------------------------------
        self.i = 1
        self.padding = 20
        # ----------------------------------------------------------------------------------------------------
        self.txt = TextInput(hint_text="Numbers", pos_hint={"x": 0, "top": 1}, size_hint=(0.5, 0.2), multiline=False)
        self.btn_add = Button(text="Add", pos_hint={"right": 1, "top": 1}, size_hint=(0.5, 0.1), disabled=True,
                              on_press=self.add_num, color="#FFFFFF", background_color="#10F5D8", font_size=20)
        self.btn_reset = Button(text="Reset", pos_hint={"right": 1, "y": 0.8}, size_hint=(0.5, 0.1), disabled=True,
                                on_press=self.Reset, color="#FFFFFF", background_color="#10F5D8", font_size=20)
        self.btn_samp = Button(text="sample variance", pos_hint={"x": 0, "y": 0.6}, size_hint=(1, 0.2), disabled=False,
                               on_press=self.which_vari_s, color="#FFFFFF", background_color="#10F5D8", font_size=20)
        self.btn_norm = Button(text="normal variance", pos_hint={"x": 0, "y": 0.4}, size_hint=(1, 0.2), disabled=False,
                               on_press=self.which_vari_n, color="#FFFFFF", background_color="#10F5D8", font_size=20)
        self.btn_ok = Button(text="Calculate", pos_hint={"x": 0.2, "y": 0.1}, size_hint=(0.6, 0.2), disabled=True,
                             on_press=self.goto, color="black", background_color="#10F5D8", font_size=20)
        self.me = Button(text="Me", pos_hint={"x": 0, "y": 0}, size_hint=(0.1, 0.1), background_color="red",
                         color="#FFFFFF", on_press=self.Me)
        # ----------------------------------------------------------------------------------------------------
        self.add_widget(self.txt)
        self.add_widget(self.btn_add)
        self.add_widget(self.btn_reset)
        self.add_widget(self.btn_samp)
        self.add_widget(self.btn_norm)
        self.add_widget(self.btn_ok)
        self.add_widget(self.me)
        # ----------------------------------------------------------------------------------------------------

    # when you choose the type of variance
    def which_vari_s(self, *args):
        """chose sample variance"""
        self.btn_samp.disabled = True
        self.btn_norm.disabled = False
        self.btn_add.disabled = False
        self.btn_reset.disabled = False
        if self.txt.hint_text == "Numbers":
            self.txt.hint_text = "1th number"
        d.append(1)

    def which_vari_n(self, *args):
        """chose normal variance"""
        self.btn_samp.disabled = False
        self.btn_norm.disabled = True
        self.btn_add.disabled = False
        self.btn_reset.disabled = False
        if self.txt.hint_text == "Numbers":
            self.txt.hint_text = "1th number"
        d.clear()

    def add_num(self, *args):
        """add one number into list"""
        Input = self.txt.text
        self.txt.text = ""
        try:
            data.append(float(Input))
            self.i += 1
            self.txt.hint_text = str(self.i) + "th number"
            if self.btn_ok.disabled == True and self.i > 2:
                self.btn_ok.disabled = False


        except ValueError:
            self.Error()

    def Me(self, *args):
        """about me"""
        self.pop = Pop_Er()
        self.pop.title = "Who made this app?"
        self.pop.lb.text = "-----KPS-----"
        self.pop.lb.background_color = "red"
        self.pop.lb.color1 = "#FFFFFF"
        self.pop.lb.font_size = 20
        self.pop.open()

    def Error(self, *args):
        """open the popup layout"""
        self.pop = Pop_Er()
        self.pop.title = "Value Error"
        self.pop.lb.text = "invalid input."
        self.pop.open()

    def Reset(self, *args):
        """clear the text in textinput and clear all data"""
        data.clear()
        self.txt.text = ""
        self.i = 1
        self.txt.hint_text = str(self.i) + "th number"
        self.btn_ok.disabled = True

    def goto(self, *args):
        """change the page and texts in second page"""
        MainScreen().switch_M_to_R()


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Win())

    def switch_M_to_R(self, *args):
        sm.transition.direction = "right"
        sm.current = "Result"
        # ----------------------------------------------------------------------------------------------------


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Win2())

    def switch_R_to_M(self, *args):
        sm.transition.direction = "left"
        sm.current = "Main"


class Scm(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget((MainScreen(name="Main")))
        self.add_widget(ResultScreen(name="Result"))

sm = Scm()


class CalculaterApp(App):
    def build(self):
        Window.size = (400, 300)
        Window.clearcolor = (1, 1, 0, 1)
        return sm


if __name__ == "__main__":
    CalculaterApp().run()
