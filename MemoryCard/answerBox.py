from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QRadioButton
import random

class MyBox(QGroupBox):
    
    def __init__(self):
        super().__init__()
        self.setTitle("Варианты ответа")
        self.resize(100,150)
        self.initUI()

    def initUI(self):
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.blue)
        self.setPalette(p)
    
# testDic = {
#             "Логотип фирмы Apple" : [QRadioButton("Яблоко"), QRadioButton("Груша"),QRadioButton("Банан"), QRadioButton("Арбуз")],
#             "Основатель  Windows" : [QRadioButton("Гомодрил Флейтс"),QRadioButton("Биолан Газманов"),QRadioButton("Билл Гейтс"),QRadioButton("Билл Гейтс")]}