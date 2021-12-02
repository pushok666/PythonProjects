from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from answerBox import MyBox
from AnswerButton import MyAnswerButton
import random
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QVBoxLayout()
        self.myBox = MyBox()
        self.myAnswerButton = MyAnswerButton()
        kyes = self.myBox.answerDic.keys()
        kyesList = list(kyes)
        self.tLayout = QLabel(random.choice(kyesList))
        self.mainLayout.addWidget(self.tLayout, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.myBox)
        self.mainLayout.addWidget(self.myAnswerButton, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.mainLayout)
        self.resize(800,600)