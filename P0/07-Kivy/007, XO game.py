from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
import random


# first popup
class MyPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.l1 = Button(text=str(FirstWindow().shownow()), background_color="yellow", color="red", font_size=40)
        self.l1.bind(on_press=self.bttn_action)
        self.size_hint=(0.3, 0.3)
        self.title = "Toss"
        self.add_widget(self.l1)

    def bttn_action(self, temp):
        self.dismiss()


# Game result popup
class MyPop(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.l2 = Button(text="", background_color="red", color="yellow", font_size=40)
        self.l2.bind(on_press=self.bttn_action2)
        self.size_hint = (0.3, 0.3)
        self.title = "Winner"
        self.add_widget(self.l2)

    def bttn_action2(self, temp):
        self.dismiss()


# first window --> Ui elements in .kv file
class FirstWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Grid_Main())


    def shownow(self):
        g=Grid_1()
        self.player1_name = g.txt1.text
        self.player2_name = g.txt2.text
        self.toss = [self.player1_name, self.player2_name]
        return self.toss[random.choice([0, 1])]

    def open_popup(self):
        pops = MyPopup()
        pops.l1.text = str(self.shownow()) + " will start first!" + "\n Click to start"
        pops.open()


class Grid_Main(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        self.add_widget(Grid_1())
        self.add_widget(Grid_2())


class Grid_1(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.lb1 = Label(text="   Player\none name", font_size=20)
        self.lb2 = Label(text="   Player \ntwo name", font_size=20)
        self.txt1 = TextInput(multiline=False, font_size=50)
        self.txt2 = TextInput(multiline=False, font_size=50)
        #######################################
        #######################################
        self.add_widget(self.lb1)
        self.add_widget(self.txt1)
        self.add_widget(self.lb2)
        self.add_widget(self.txt2)

class Grid_2(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 1
        self.cols = 1
        self.btn = Button(text= "toss", font_size=50)
        self.btn.bind(on_press=FirstWindow.open_popup)
        self.add_widget(self.btn)


class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(tab2())


class tab2(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.option = ["O", "X"]
        self.count = 0
        self.padding = (20, 20)
        # -------------------------------------------------------------------------------------
        # user input
        self.current_value = 2
        self.cols = 3
        self.rows = 4
        # --------------------------------------------------------------------------------------
        self.btn_xo = Button(text="choose X or O", font_size=20)
        self.add_widget(self.btn_xo)
        self.input_option = TextInput(font_size=100)
        self.add_widget(self.input_option)
        self.btn_enter = Button(text="Enter")
        self.btn_enter.bind(on_press=self.bttn)
        self.add_widget(self.btn_enter)

        # --------------------------------------------------------------------------------------

        if str(self.btn_enter.text).upper() == "X" or str(self.btn_enter.text).upper() == "O":
            self.spacing = (5, 5)
            # -----------------------
            self.b1 = Button(text="", font_size=150, Background_color="blue")
            self.b1.bind(on_press=self.bttn1)
            self.add_widget(self.b1)
            # -----------------------
            self.b2 = Button(text="", font_size=150, Background_color="blue")
            self.b2.bind(on_press=self.bttn2)
            self.add_widget(self.b2)
            # -----------------------
            self.b3 = Button(text="", font_size=150)
            self.b3.bind(on_press=self.bttn3)
            self.add_widget(self.b3)
            # -----------------------
            self.b4 = Button(text="", font_size=150)
            self.b4.bind(on_press=self.bttn4)
            self.add_widget(self.b4)
            # -----------------------
            self.b5 = Button(text="", font_size=150)
            self.b5.bind(on_press=self.bttn5)
            self.add_widget(self.b5)
            # -----------------------
            self.b6 = Button(text="", font_size=150)
            self.b6.bind(on_press=self.bttn6)
            self.add_widget(self.b6)
            # -----------------------
            self.b7 = Button(text="", font_size=150)
            self.b7.bind(on_press=slf.bttn7)
            self.add_widget(self.b7)
            # -----------------------
            self.b8 = Button(text="", font_size=150)
            self.b8.bind(on_press=self.bttn8)
            self.add_widget(self.b8)
            # -----------------------
            self.b9 = Button(text="", font_size=150)
            self.b9.bind(on_press=self.bttn9)
            self.add_widget(self.b9)
            # ------------------------

    # ------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------
    def bttn(self, instance):
        self.all_button_active_or_diactive(True)
        a = str(self.input_option.text)
        a = a.upper()

        if a == "X":
            self.current_value = 1
        elif a == "O":
            self.current_value = 0
        else:
            pass

    #########################################################

    #########################################################
    def bttn1(self, instances):
        self.result()
        if self.b1.text == "X" or self.b1.text == "O":
            print("select other options")
        else:
            self.count += 1
            self.b1.text = self.option[self.current_value]
            if self.current_value == 1:
                self.current_value = 0
            elif self.current_value == 0:
                self.current_value = 1
            self.b1.disabled = True
            self.result()

    ######################################################

    ######################################################
    def bttn2(self, instances):
        self.result()
        if self.b2.text == "X" or self.b2.text == "O":
            print("select other options")
        else:
            self.count += 1
            self.b2.text = self.option[self.current_value]
            if self.current_value == 1:
                self.current_value = 0
            elif self.current_value == 0:
                self.current_value = 1
            self.b2.disabled = True
            print("pressed")
            self.result()

    ######################################################

    ######################################################
    def bttn3(self, instances):
        self.result()
        if self.b3.text == "X" or self.b3.text == "O":
            print("select other options")
        else:
            self.count += 1
            self.b3.text = self.option[self.current_value]
            if self.current_value == 1:
                self.current_value = 0
            elif self.current_value == 0:
                self.current_value = 1
            self.b3.disabled = True
            print("pressed")
            self.result()

    ######################################################

    ######################################################
    def bttn4(self, instances):
        self.result()
        if self.b4.text == "X" or self.b4.text == "O":
            print("select other options")
        else:
            self.count += 1
            self.b4.text = self.option[self.current_value]
            if self.current_value == 1:
                self.current_value = 0
            elif self.current_value == 0:
                self.current_value = 1
            self.b4.disabled = True
            print("pressed")
            self.result()

    ######################################################

    ######################################################
    def bttn5(self, instances):
        self.result()
        if self.b5.text == "X" or self.b5.text == "O":
            print("select other options")
        else:
            self.count += 1
            self.b5.text = self.option[self.current_value]
            if self.current_value == 1:
                self.current_value = 0
            elif self.current_value == 0:
                self.current_value = 1
            self.b5.disabled = True
            print("pressed")
            self.result()

    ######################################################

    ######################################################
    def bttn6(self, instances):
        self.result()
        if self.b6.text == "X" or self.b6.text == "O":
            print("select other options")
        else:
            self.count += 1
            self.b6.text = self.option[self.current_value]
            if self.current_value == 1:
                self.current_value = 0
            elif self.current_value == 0:
                self.current_value = 1
            self.b6.disabled = True
            print("pressed")
            self.result()

    ######################################################

    ######################################################
    def bttn7(self, instances):
        self.result()
        if self.b7.text == "X" or self.b7.text == "O":
            print("select other options")
        else:
            self.count += 1
            self.b7.text = self.option[self.current_value]
            if self.current_value == 1:
                self.current_value = 0
            elif self.current_value == 0:
                self.current_value = 1
            self.b7.disabled = True
            print("pressed")
            self.result()

    ######################################################

    ######################################################
    def bttn8(self, instances):
        self.result()
        if self.b8.text == "X" or self.b8.text == "O":
            print("select other options")
        else:
            self.count += 1
            self.b8.text = self.option[self.current_value]
            if self.current_value == 1:
                self.current_value = 0
            elif self.current_value == 0:
                self.current_value = 1
            self.b8.disabled = True
            print("pressed")
            self.result()

    ######################################################

    ######################################################
    def bttn9(self, instances):
        self.result()
        if self.b9.text == "X" or self.b9.text == "O":
            print("select other options")
        else:
            self.count += 1
            self.b9.text = self.option[self.current_value]
            if self.current_value == 1:
                self.current_value = 0
            elif self.current_value == 0:
                self.current_value = 1
            self.b9.disabled = True
            print("pressed")
            self.result()

    ######################################################

    ######################################################
    def resutl(self):
        if self.b1.text == "X" and self.b2.text == "X" and self.b3.text == "X":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "X is the winner"
            self.back()
        elif self.b4.text == "X" and self.b5.text == "X" and self.b6.text == "X":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "X is the winner"
            self.back()
        elif self.b7.text == "X" and self.b8.text == "X" and self.b9.text == "X":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "X is the winner"
            self.back()
        elif self.b1.text == "X" and self.b4.text == "X" and self.b7.text == "X":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "X is the winner"
            self.back()
        elif self.b2.text == "X" and self.b5.text == "X" and self.b8.text == "X":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "X is the winner"
            self.back()
        elif self.b3.text == "X" and self.b6.text == "X" and self.b9.text == "X":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "X is the winner"
            self.back()
        elif self.b1.text == "O" and self.b2.text == "O" and self.b3.text == "O":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "O is the winner"
            self.back()
        elif self.b4.text == "O" and self.b5.text == "O" and self.b6.text == "O":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "O is the winner"
            self.back()
        elif self.b7.text == "O" and self.b8.text == "O" and self.b9.text == "O":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "O is the winner"
            self.back()
        elif self.b1.text == "O" and self.b4.text == "O" and self.b7.text == "O":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "O is the winner"
            self.back()
        elif self.b2.text == "O" and self.b5.text == "O" and self.b8.text == "O":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "O is the winner"
            self.back()
        elif self.b3.text == "O" and self.b6.text == "O" and self.b9.text == "O":
            self.all_buttn_Activate_or_Deactivate(True)
            self.ans = "O is the winner"
            self.back()

    def back(self):
        pop = MyPop()
        pop.l2.text = self.ans
        pop.open()


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FirstWindow(name="sign"))
        self.add_widget(SecondWindow(name="game"))


kv = Manager()


class XOgameApp(App):
    def build(self):
        self.title = "XO Game"
        return kv


if __name__ == "__main__":
    XOgameApp().run()
