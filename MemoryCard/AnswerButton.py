from PyQt5.QtWidgets import QPushButton

def Button_Click():
    print("fff")

class MyAnswerButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("test button")
        self.clicked.connect(Button_Click)