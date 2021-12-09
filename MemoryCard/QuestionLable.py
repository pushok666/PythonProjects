from PyQt5.QtWidgets import QLabel

from BissnesLogic import BL

class questionLable(QLabel):
    def __init__(self):
        super().__init__()
        bl = BL()
        self.setText(bl.lable)
        