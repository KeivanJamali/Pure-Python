# import statistics, math
#
#
# def variance_s():
#     a = []
#     dic={}
#     b, c, i = 0, 0, 1
#     while True:
#         b = input("number " + str(i) + " ?: ")
#         try:
#             c += float(b)
#             a.append(float(b))
#             i += 1
#         except ValueError:
#             print("invalid, continue?", end=" :")
#             ans = input("")
#             if ans.capitalize() == "Yes":
#                 pass
#             elif ans.capitalize() == "No":
#                 break
#
#     dic["miangin"] = c / len(a)
#     dic['variance_s'] = statistics.variance(a)
#     dic['enheraf_meyar'] = math.sqrt(dic['variance_s'])
#     dic['enheraf_meyar miangin'] = dic['enheraf_meyar'] / math.sqrt(len(a))
#     return dic
#
# print(variance_s())

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class AM(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text="ab", on_press= self.CH)
        self.add_widget(self.btn)
    def CH(self,*args):
        self.btn.text = str(9)

class C():
    global x
    x = []

    def i(self):
        AM.btn.text = "567"


class asApp(App):
    def build(self):
        s = AM()
        return s
C().i()
asApp().run()
