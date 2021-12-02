from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QRadioButton
import random

class MyBox(QGroupBox):
    
    def __init__(self):
        super().__init__()
        self.answerDic = {"Логотип фирмы Apple" : [QRadioButton("Яблоко"), QRadioButton("Груша"),QRadioButton("Банан"), QRadioButton("Арбуз")]}
        answerList = list(self.answerDic.values())
        self.mainLayout = QVBoxLayout()
        #self.mainLayout.addWidget(answerList[0][0])
        for item in answerList:
            for answer in item:
                self.mainLayout.addWidget(answer)
        self.setTitle("Варианты ответа")
        self.resize(100,150)
        #self.setStyleSheet("background-color: yellow;")
        #self.setBox()
        self.setLayout(self.mainLayout)
        self.initUI()

    def initUI(self):
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)
    # def setBox(self):
    #     answerList = list(self.answerDic.values())
    #     for item in answerList:
    #         self.layout.addWidget(item)
        
    #buttonLayout = QButtonGroup()

