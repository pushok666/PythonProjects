from PyQt5.QtWidgets import QRadioButton
import random

class BL():
    def __init__(self):
        self.data = {
            "Логотип фирмы Apple" : [QRadioButton("Яблоко"), QRadioButton("Груша"),QRadioButton("Банан"), QRadioButton("Арбуз")],
            "Основатель  Windows" : [QRadioButton("Гомодрил Флейтс"),QRadioButton("Биолан Газманов"),QRadioButton("Билл Гейтс"),QRadioButton("Билл Гейтс")]}
        lables = list(self.data.keys())
        self.lable = random.choice(lables)