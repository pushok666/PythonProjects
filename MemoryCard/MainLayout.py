from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout
from AnswerButton import MyAnswerButton

from QuestionLable import questionLable
from answerBox import MyBox

class mainVLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        lable = questionLable()
        boxAnswer = MyBox()
        button = MyAnswerButton()
        self.addWidget(lable, alignment=Qt.AlignmentFlag.AlignCenter)
        self.addWidget(boxAnswer, alignment=Qt.AlignmentFlag.AlignCenter)
        self.addWidget(button, stretch=1)
        