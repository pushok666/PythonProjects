from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


app = QApplication([])#создание объекта приложения
main_win = QWidget()#создание окна
main_win.move(500,500)#установка размера окна
main_win.setWindowTitle("My Firs PyQt App!") #заголовок главного окна
hello_text = QLabel("Hello Windows")#запись в окне

line_map = QVBoxLayout()
line_map.addWidget(hello_text, alignment = Qt.AlignCenter)#отрисовка записи по цетру
main_win.setLayout(line_map)#добавление записи в окно   

main_win.show()
app.exec_()