from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.core.window import Window
import math
from kivy.uix.popup import Popup

Data = {"Sagar Ahmadi": {"Birthday": "1381/01/08", "pic": "Ahmadi.jpg"},
        "Nima Ariaii": {"Birthday": "1380/12/16", "pic": "Ariaii.jpg"},
        "Yasamin Ariaiirad": {"Birthday": "1380/11/26", "pic": "Ariaiirad.jpg"},
        "Ayda Asadi": {"Birthday": "1381/04/11", "pic": "Asadi.jpg"},
        "Varta Balash": {"Birthday": "1381/01/06", "pic": "Balash.jpg"},
        "Alireza Bodagi": {"Birthday": "1380/12/11", "pic": "Bodagi(Ali).jpg"},
        "Amirhosein Bodagi": {"Birthday": "1381/04/10", "pic": "Bodagi(Amir).jpg"},
        "Hosein Charmahali": {"Birthday": "1380/09/29", "pic": "Charmahali.jpg"},
        "Zohre Drodian": {"Birthday": "1380/09/22", "pic": "Drodian.jpg"},
        "Mahshad Firoze": {"Birthday": "1380/09/04", "pic": "Firoze.jpg"},
        "Amirhosein Ganbari": {"Birthday": "1380/10/08", "pic": "Ganbari.jpg"},
        "Omidreza Garabadiyan": {"Birthday": "1380/09/02",
                                 "pic": "Garabadiyan(Omid).jpg"},
        "Poya Hadizade": {"Birthday": "1381/01/11", "pic": "Hadizade.jpg"},
        "Keivan Jamali": {"Birthday": "1380/10/05", "pic": "Jamali.jpg"},
        "Arsam Maroufi": {"Birthday": "1381/05/31", "pic": "Maroufi.jpg"},
        "Meysam Matin": {"Birthday": "1381/06/14", "pic": "Matin.jpg"},
        "Sepehr Mazaheri": {"Birthday": "1381/01/02", "pic": "Mazaheri.jpg"},
        "Mahdi Mirabdolaii": {"Birthday": "1380/12/20", "pic": "Mirabdolaii.jpg"},
        "Narges Motavali": {"Birthday": "1380/12/24", "pic": "Motavali.jpg"},
        "Mani Nilchian": {"Birthday": "1381/04/04", "pic": "Nilchian.jpg"},
        "Arian Porasad": {"Birthday": "1381/06/30", "pic": "Porasad.jpg"},
        "Ali Rahimi": {"Birthday": "1380/07/25", "pic": "Rahimi(Ali).jpg"},
        "Amirmohammad Rahimi": {"Birthday": "1380/09/08", "pic": "Rahimi(Amir).jpg"},
        "Shayan Raoufi": {"Birthday": "1380/08/28", "pic": "Raoufi.jpg"},
        "Yousof Rezaii": {"Birthday": "1381/06/10", "pic": "Rezaii.jpg"},
        "Poya Shamsipour": {"Birthday": "1380/07/17", "pic": "Shamsipour.jpg"},
        "Paniz Sormanshahi": {"Birthday": "1381/05/10", "pic": "Sormanshahi.jpg"},
        "Mahdi Tabasi": {"Birthday": "1380/11/28", "pic": "Tabasi.jpg"},
        "mamad Tagavi": {"Birthday": "1381/06/27", "pic": "Tagavi.jpg"},
        "Ali Taheri": {"Birthday": "1381/06/26", "pic": "Taheri.jpg"},
        "Mahyar Zafarkhah": {"Birthday": "1380/09/06", "pic": "Zafarkhah.jpg"},
        "Hosein Sharifi": {"Birthday": "1381/01/26", "pic": "unknown.jpg"},
        "Nima Mohammadnia": {"Birthday": "1381/02/05", "pic": "unknown.jpg"},
        "Mojtaba Sajadi": {"Birthday": "1381/02/19", "pic": "unknown.jpg"},
        "Nasrin Sharifi": {"Birthday": "1381/02/29", "pic": "unknown.jpg"},
        "Mahdi AlBoye": {"Birthday": "1381/03/11", "pic": "unknown.jpg"},
        "Yasin Anaraki": {"Birthday": "1381/03/22", "pic": "unknown.jpg"},
        "Mohammadfazel Heidari": {"Birthday": "1381/04/15", "pic": "unknown.jpg"},
        "Fateme Mahdi": {"Birthday": "1381/05/11", "pic": "unknown.jpg"},
        "Ramtin Faragi": {"Birthday": "1381/05/31", "pic": "unknown.jpg"},
        "Ali Mohades": {"Birthday": "1381/05/31", "pic": "unknown.jpg"},
        "Ali Mosaiebi": {"Birthday": "1381/06/29", "pic": "unknown.jpg"},
        "Mohammad Borhani": {"Birthday": "1380/09/05", "pic": "unknown.jpg"},
        "Amirhosein Ranjbar": {"Birthday": "1380/09/19", "pic": "unknown.jpg"},
        "Sana Mansori": {"Birthday": "1380/10/05", "pic": "unknown.jpg"},
        "Ali Javaheri": {"Birthday": "1380/10/13", "pic": "unknown.jpg"},
        "Ariyana Khezri": {"Birthday": "1380/11/03", "pic": "unknown.jpg"},
        "Aliraza Sarkar": {"Birthday": "1380/11/18", "pic": "unknown.jpg"},
        "Ariyana Yavari": {"Birthday": "1380/11/29", "pic": "unknown.jpg"},
        "Mohammadamin Hashemi": {"Birthday": "1380/12/16", "pic": "unknown.jpg"},
        "Amin Garabadiyan": {"Birthday": "1380/12/20", "pic": "unknown.jpg"},
        "Hosein Ansari": {"Birthday": "1380/12/23", "pic": "unknown.jpg"},
        }


class Pop(Popup):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.bbt = Button(text="", size_hint=(0.2, 0.1))
        self.bbt.bind(on_press=self.act)
        self.add_widget(self.bbt)

    def act(self, *args):
        self.dismiss()


class Win(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 5
        self.spacing = 2
        self.sc_x = float(Window.size[0])
        self.sc_y = float(Window.size[1])
        self.btn1 = Button(text="Sagar Ahmadi", font_size=13, size_hint=(0.166, 0.1),
                           background_color="#FFFB00",
                           on_press=lambda x: self.open(b=Data["Sagar Ahmadi"]["Birthday"],
                                                        p=Data["Sagar Ahmadi"]["pic"], a="Sagar Ahmadi"))
        self.btn2 = Button(text="Nima Ariaii", font_size=13, size_hint=(0.166, 0.1),
                           background_color="#FF7B00",
                           on_press=lambda x: self.open(b=Data["Nima Ariaii"]["Birthday"],
                                                        p=Data["Nima Ariaii"]["pic"], a="Nima Ariaii"))
        self.btn3 = Button(text="Yasamin Ariaiirad", font_size=math.sqrt(self.sc_x * self.sc_y) / 50,
                           size_hint=(0.166, 0.1),
                           background_color="#FFFB00",
                           on_press=lambda x: self.open(b=Data["Yasamin Ariaiirad"]["Birthday"],
                                                        p=Data["Yasamin Ariaiirad"]["pic"], a="Yasamin Ariaiirad"))
        self.btn4 = Button(text="Ayda Asadi", font_size=13, size_hint=(0.166, 0.1),
                           background_color="#FF7B00",
                           on_press=lambda x: self.open(b=Data["Ayda Asadi"]["Birthday"],
                                                        p=Data["Ayda Asadi"]["pic"], a="Ayda Asadi"))
        self.btn5 = Button(text="Varta Balash", font_size=15, size_hint=(0.166, 0.1),
                           background_color="#FFFB00",
                           on_press=lambda x: self.open(b=Data["Varta Balash"]["Birthday"],
                                                        p=Data["Varta Balash"]["pic"], a="Varta Balash"))
        self.btn6 = Button(text="Alireza Bodagi", font_size=13, size_hint=(0.166, 0.1),
                           background_color="#FF7B00",
                           on_press=lambda x: self.open(b=Data["Alireza Bodagi"]["Birthday"],
                                                        p=Data["Alireza Bodagi"]["pic"], a="Alireza Bodagi"))
        self.btn7 = Button(text="Amirhosein Bodagi", font_size=13, size_hint=(0.166, 0.1),
                           background_color="#00FFE6",
                           on_press=lambda x: self.open(b=Data["Amirhosein Bodagi"]["Birthday"],
                                                        p=Data["Amirhosein Bodagi"]["pic"], a="Amirhosein Bodagi"))
        self.btn8 = Button(text="Hosein Charmahali", font_size=13, size_hint=(0.166, 0.1),
                           background_color="#00FF06",
                           on_press=lambda x: self.open(b=Data["Hosein Charmahali"]["Birthday"],
                                                        p=Data["Hosein Charmahali"]["pic"], a="Hosein Charmahali"))
        self.btn9 = Button(text="Zohre Drodian", font_size=13, size_hint=(0.166, 0.1),
                           background_color="#00FFE6",
                           on_press=lambda x: self.open(b=Data["Zohre Drodian"]["Birthday"],
                                                        p=Data["Zohre Drodian"]["pic"], a="Zohre Drodian"))
        self.btn10 = Button(text="Mahshad Firoze", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FF06",
                            on_press=lambda x: self.open(b=Data["Mahshad Firoze"]["Birthday"],
                                                         p=Data["Mahshad Firoze"]["pic"], a="Mahshad Firoze"))
        self.btn11 = Button(text="Amirhosein Ganbari", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FFE6",
                            on_press=lambda x: self.open(b=Data["Amirhosein Ganbari"]["Birthday"],
                                                         p=Data["Amirhosein Ganbari"]["pic"], a="Amirhosein Ganbari"))
        self.btn12 = Button(text="Omidreza Garabadiyan", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FF06",
                            on_press=lambda x: self.open(b=Data["Omidreza Garabadiyan"]["Birthday"],
                                                         p=Data["Omidreza Garabadiyan"]["pic"],
                                                         a="Omidreza Garabadiyan"))
        self.btn13 = Button(text="Poya Hadizade", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FFFB00",
                            on_press=lambda x: self.open(b=Data["Poya Hadizade"]["Birthday"],
                                                         p=Data["Poya Hadizade"]["pic"], a="Poya Hadizade"))
        self.btn14 = Button(text="Keivan Jamali", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FF7B00",
                            on_press=lambda x: self.open(b=Data["Keivan Jamali"]["Birthday"],
                                                         p=Data["Keivan Jamali"]["pic"], a="Keivan Jamali"))
        self.btn15 = Button(text="Arsam Maroufi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FFFB00",
                            on_press=lambda x: self.open(b=Data["Arsam Maroufi"]["Birthday"],
                                                         p=Data["Arsam Maroufi"]["pic"], a="Arsam Maroufi"))
        self.btn16 = Button(text="Meysam Matin", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FF7B00",
                            on_press=lambda x: self.open(b=Data["Meysam Matin"]["Birthday"],
                                                         p=Data["Meysam Matin"]["pic"], a="Meysam Matin"))
        self.btn17 = Button(text="Sepehr Mazaheri", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FFFB00",
                            on_press=lambda x: self.open(b=Data["Sepehr Mazaheri"]["Birthday"],
                                                         p=Data["Sepehr Mazaheri"]["pic"], a="Sepehr Mazaheri"))
        self.btn18 = Button(text="Mahdi Mirabdolaii", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FF7B00",
                            on_press=lambda x: self.open(b=Data["Mahdi Mirabdolaii"]["Birthday"],
                                                         p=Data["Mahdi Mirabdolaii"]["pic"], a="Mahdi Mirabdolaii"))
        self.btn19 = Button(text="Narges Motavali", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FFE6",
                            on_press=lambda x: self.open(b=Data["Narges Motavali"]["Birthday"],
                                                         p=Data["Narges Motavali"]["pic"], a="Narges Motavali"))
        self.btn20 = Button(text="Mani Nilchian", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FF06",
                            on_press=lambda x: self.open(b=Data["Mani Nilchian"]["Birthday"],
                                                         p=Data["Mani Nilchian"]["pic"], a="Mani Nilchian"))
        self.btn21 = Button(text="Arian Porasad", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FFE6",
                            on_press=lambda x: self.open(b=Data["Arian Porasad"]["Birthday"],
                                                         p=Data["Arian Porasad"]["pic"], a="Arian Porasad"))
        self.btn22 = Button(text="Ali Rahimi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FF06",
                            on_press=lambda x: self.open(b=Data["Ali Rahimi"]["Birthday"],
                                                         p=Data["Ali Rahimi"]["pic"], a="Ali Rahimi"))
        self.btn23 = Button(text="Amirmohammad Rahimi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FFE6",
                            on_press=lambda x: self.open(b=Data["Amirmohammad Rahimi"]["Birthday"],
                                                         p=Data["Amirmohammad Rahimi"]["pic"], a="Amirmohammad Rahimi"))
        self.btn24 = Button(text="Shayan Raoufi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FF06",
                            on_press=lambda x: self.open(b=Data["Shayan Raoufi"]["Birthday"],
                                                         p=Data["Shayan Raoufi"]["pic"], a="Shayan Raoufi"))
        self.btn25 = Button(text="Yousof Rezaii", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FFFB00",
                            on_press=lambda x: self.open(b=Data["Yousof Rezaii"]["Birthday"],
                                                         p=Data["Yousof Rezaii"]["pic"], a="Yousof Rezaii"))
        self.btn26 = Button(text="Poya Shamsipour", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FF7B00",
                            on_press=lambda x: self.open(b=Data["Poya Shamsipour"]["Birthday"],
                                                         p=Data["Poya Shamsipour"]["pic"], a="Poya Shamsipour"))
        self.btn27 = Button(text="Paniz Sormanshahi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FFFB00",
                            on_press=lambda x: self.open(b=Data["Paniz Sormanshahi"]["Birthday"],
                                                         p=Data["Paniz Sormanshahi"]["pic"], a="Paniz Sormanshahi"))
        self.btn28 = Button(text="Mahdi Tabasi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FF7B00",
                            on_press=lambda x: self.open(b=Data["Mahdi Tabasi"]["Birthday"],
                                                         p=Data["Mahdi Tabasi"]["pic"], a="Mahdi Tabasi"))
        self.btn29 = Button(text="mamad Tagavi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FFFB00",
                            on_press=lambda x: self.open(b=Data["mamad Tagavi"]["Birthday"],
                                                         p=Data["mamad Tagavi"]["pic"], a="mamad Tagavi"))
        self.btn30 = Button(text="Ali Taheri", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FF7B00",
                            on_press=lambda x: self.open(b=Data["Ali Taheri"]["Birthday"],
                                                         p=Data["Ali Taheri"]["pic"], a="Ali Taheri"))
        self.btn31 = Button(text="Mahyar Zafarkhah", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FFE6",
                            on_press=lambda x: self.open(b=Data["Mahyar Zafarkhah"]["Birthday"],
                                                         p=Data["Mahyar Zafarkhah"]["pic"], a="Mahyar Zafarkhah"))
        self.btn32 = Button(text="Hosein Sharifi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FF06",
                            on_press=lambda x: self.open(b=Data["Hosein Sharifi"]["Birthday"],
                                                         p=Data["Hosein Sharifi"]["pic"], a="Hosein Sharifi"))
        self.btn33 = Button(text="Nima Mohammadnia", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FFE6",
                            on_press=lambda x: self.open(b=Data["Nima Mohammadnia"]["Birthday"],
                                                         p=Data["Nima Mohammadnia"]["pic"], a="Nima Mohammadnia"))
        self.btn34 = Button(text="Mojtaba Sajadi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FF06",
                            on_press=lambda x: self.open(b=Data["Mojtaba Sajadi"]["Birthday"],
                                                         p=Data["Mojtaba Sajadi"]["pic"], a="Mojtaba Sajadi"))
        self.btn35 = Button(text="Nasrin Sharifi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FFE6",
                            on_press=lambda x: self.open(b=Data["Nasrin Sharifi"]["Birthday"],
                                                         p=Data["Nasrin Sharifi"]["pic"], a="Nasrin Sharifi"))
        self.btn36 = Button(text="Mahdi AlBoye", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FF06",
                            on_press=lambda x: self.open(b=Data["Mahdi AlBoye"]["Birthday"],
                                                         p=Data["Mahdi AlBoye"]["pic"], a="Mahdi AlBoye"))
        self.btn37 = Button(text="Yasin Anaraki", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FFFB00",
                            on_press=lambda x: self.open(b=Data["Yasin Anaraki"]["Birthday"],
                                                         p=Data["Yasin Anaraki"]["pic"], a="Yasin Anaraki"))
        self.btn38 = Button(text="Mohammadfazel Heidari", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FF7B00",
                            on_press=lambda x: self.open(b=Data["Mohammadfazel Heidari"]["Birthday"],
                                                         p=Data["Mohammadfazel Heidari"]["pic"],
                                                         a="Mohammadfazel Heidari"))
        self.btn39 = Button(text="Fateme Mahdi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FFFB00",
                            on_press=lambda x: self.open(b=Data["Fateme Mahdi"]["Birthday"],
                                                         p=Data["Fateme Mahdi"]["pic"], a="Fateme Mahdi"))
        self.btn40 = Button(text="Ramtin Faragi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FF7B00",
                            on_press=lambda x: self.open(b=Data["Ramtin Faragi"]["Birthday"],
                                                         p=Data["Ramtin Faragi"]["pic"], a="Ramtin Faragi"))
        self.btn41 = Button(text="Ali Mohades", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FFFB00",
                            on_press=lambda x: self.open(b=Data["Ali Mohades"]["Birthday"],
                                                         p=Data["Ali Mohades"]["pic"], a="Ali Mohades"))
        self.btn42 = Button(text="Ali Mosaiebi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FF7B00",
                            on_press=lambda x: self.open(b=Data["Ali Mosaiebi"]["Birthday"],
                                                         p=Data["Ali Mosaiebi"]["pic"], a="Ali Mosaiebi"))
        self.btn43 = Button(text="Mohammad Borhani", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FFE6",
                            on_press=lambda x: self.open(b=Data["Mohammad Borhani"]["Birthday"],
                                                         p=Data["Mohammad Borhani"]["pic"], a="Mohammad Borhani"))
        self.btn44 = Button(text="Amirhosein Ranjbar", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FF06",
                            on_press=lambda x: self.open(b=Data["Amirhosein Ranjbar"]["Birthday"],
                                                         p=Data["Amirhosein Ranjbar"]["pic"], a="Amirhosein Ranjbar"))
        self.btn45 = Button(text="Sana Mansori", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FFE6",
                            on_press=lambda x: self.open(b=Data["Sana Mansori"]["Birthday"],
                                                         p=Data["Sana Mansori"]["pic"], a="Sana Mansori"))
        self.btn46 = Button(text="Ali Javaheri", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FF06",
                            on_press=lambda x: self.open(b=Data["Ali Javaheri"]["Birthday"],
                                                         p=Data["Ali Javaheri"]["pic"], a="Ali Javaheri"))
        self.btn47 = Button(text="Ariyana Khezri", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FFE6",
                            on_press=lambda x: self.open(b=Data["Ariyana Khezri"]["Birthday"],
                                                         p=Data["Ariyana Khezri"]["pic"], a="Ariyana Khezri"))
        self.btn48 = Button(text="Aliraza Sarkar", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#00FF06",
                            on_press=lambda x: self.open(b=Data["Aliraza Sarkar"]["Birthday"],
                                                         p=Data["Aliraza Sarkar"]["pic"], a="Aliraza Sarkar"))
        self.btn49 = Button(text="Ariyana Yavari", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FFFB00",
                            on_press=lambda x: self.open(b=Data["Ariyana Yavari"]["Birthday"],
                                                         p=Data["Ariyana Yavari"]["pic"], a="Ariyana Yavari"))
        self.btn50 = Button(text="Mohammadamin Hashemi", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FF7B00",
                            on_press=lambda x: self.open(b=Data["Mohammadamin Hashemi"]["Birthday"],
                                                         p=Data["Mohammadamin Hashemi"]["pic"],
                                                         a="Mohammadamin Hashemi"))
        self.btn51 = Button(text="Amin Garabadiyan", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FFFB00",
                            on_press=lambda x: self.open(b=Data["Amin Garabadiyan"]["Birthday"],
                                                         p=Data["Amin Garabadiyan"]["pic"], a="Amin Garabadiyan"))
        self.btn52 = Button(text="Hosein Ansari", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FF7B00",
                            on_press=lambda x: self.open(b=Data["Hosein Ansari"]["Birthday"],
                                                         p=Data["Hosein Ansari"]["pic"], a="Hosein Ansari"))
        self.btn53 = Button(text="Me", font_size=13, size_hint=(0.166, 0.1),
                            background_color="#FC00FF",
                            on_press=lambda x: self.open(b=Data["Keivan Jamali"]["Birthday"],
                                                         p=Data["Keivan Jamali"]["pic"], a="Keivan Jamali"))
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)
        self.add_widget(self.btn4)
        self.add_widget(self.btn5)
        self.add_widget(self.btn6)
        self.add_widget(self.btn7)
        self.add_widget(self.btn8)
        self.add_widget(self.btn9)
        self.add_widget(self.btn10)
        self.add_widget(self.btn11)
        self.add_widget(self.btn12)
        self.add_widget(self.btn13)
        self.add_widget(self.btn14)
        self.add_widget(self.btn15)
        self.add_widget(self.btn16)
        self.add_widget(self.btn17)
        self.add_widget(self.btn18)
        self.add_widget(self.btn19)
        self.add_widget(self.btn20)
        self.add_widget(self.btn21)
        self.add_widget(self.btn22)
        self.add_widget(self.btn23)
        self.add_widget(self.btn24)
        self.add_widget(self.btn25)
        self.add_widget(self.btn26)
        self.add_widget(self.btn27)
        self.add_widget(self.btn28)
        self.add_widget(self.btn29)
        self.add_widget(self.btn30)
        self.add_widget(self.btn31)
        self.add_widget(self.btn32)
        self.add_widget(self.btn33)
        self.add_widget(self.btn34)
        self.add_widget(self.btn35)
        self.add_widget(self.btn36)
        self.add_widget(self.btn37)
        self.add_widget(self.btn38)
        self.add_widget(self.btn39)
        self.add_widget(self.btn40)
        self.add_widget(self.btn41)
        self.add_widget(self.btn42)
        self.add_widget(self.btn43)
        self.add_widget(self.btn44)
        self.add_widget(self.btn45)
        self.add_widget(self.btn46)
        self.add_widget(self.btn47)
        self.add_widget(self.btn48)
        self.add_widget(self.btn49)
        self.add_widget(self.btn50)
        self.add_widget(self.btn51)
        self.add_widget(self.btn52)
        self.add_widget(self.btn53)

        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------

    def open(self, *args, **kwargs):
        self.popp = Pop()
        self.popp.bbt.text = kwargs["b"]
        self.popp.background = kwargs["p"]
        self.popp.title = kwargs["a"]
        self.popp.title_color = "black"
        self.popp.title_size = 30
        self.popp.open()


class CivilApp(App):
    def build(self):
        return Win()


CivilApp().run()
