from PyQt5.QtWidgets import QApplication
import sys
from testQWidget import MyWidget 

if __name__ == '__main__':
    app = QApplication([])
    win = MyWidget()
    win.show()
    sys.exit(app.exec_())

