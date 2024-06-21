import sys

from PyQt5.QtWidgets import *


class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)

label = QLabel("이게 프린트구나")

label.show()
# window = Mywindow()
# window.show()
app.exec_()