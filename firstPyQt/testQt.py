from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

def button_do():
    print('simple action button')

app = QApplication([])#создание объекта приложения
main_win = QWidget()#создание окна
main_win.setWindowTitle("My Firs PyQt App!") #заголовок главного окна
hello_text = QLabel("Hello Windows")#запись в окне
button = QPushButton('Сгенерировать')

line_map = QVBoxLayout()
line_map.addWidget(hello_text, alignment = Qt.AlignCenter)#отрисовка записи по цетру
line_map.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(line_map)#добавление записи в окно   

button.clicked.connect(button_do)


main_win.resize(800,600)
main_win.show()
app.exec_()


