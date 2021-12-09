from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from MainLayout import mainVLayout
from answerBox import MyBox
from AnswerButton import MyAnswerButton
import random
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = mainVLayout()
        self.setLayout(self.mainLayout)
        self.resize(800,600)