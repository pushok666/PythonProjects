from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QRadioButton
import random

from BissnesLogic import BL

class MyBox(QGroupBox):
    
    def __init__(self):
        super().__init__()
        self.setTitle("Варианты ответа")
        self.resize(100,150)
        self.initUI()
        self.addRadioButton()

    def initUI(self):
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.blue)
        self.setPalette(p)
    def addRadioButton(self):
        testlayout = QVBoxLayout()
        bl = BL()
        for item in bl.data[bl.lable]:
            testlayout.addWidget(item, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(testlayout)

    
# testDic = {
#             "Логотип фирмы Apple" : [QRadioButton("Яблоко"), QRadioButton("Груша"),QRadioButton("Банан"), QRadioButton("Арбуз")],
#             "Основатель  Windows" : [QRadioButton("Гомодрил Флейтс"),QRadioButton("Биолан Газманов"),QRadioButton("Билл Гейтс"),QRadioButton("Билл Гейтс")]}