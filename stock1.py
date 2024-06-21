import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *






# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         btn = QPushButton("버튼", self)
#         btn.move(10, 100)
#         btn.clicked.connect(self.btn_clicked)

#     def btn_clicked(self):
#         print('버튼 클릭됨')

# app = QApplication(sys.argv)
# win = MyWindow()
# win.show()
# app.exec_()
# ----------------------
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('menu.jpg'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('나가기')
        exitAction.triggered.connect(qApp.quit)

        print_action = QAction(QIcon('menu.jpg'), 'Print', self)
        print_action.setShortcut('Ctrl+P')
        print_action.setStatusTip('Print a message')
        # print_action.triggered.connect(self.show('aaa'))

        self.toolBar = self.addToolBar('Exit') 
        self.toolBar.addAction(exitAction)
        
        self.toolBar = self.addToolBar('print') 
        self.toolBar = self.addAction(print_action)

        self.statusBar()

        # menubar = self.menuBar()
        # menubar.setNativeMenuBar(False)
        # filemenu = menubar.addMenu('&File')
        # filemenu.addAction(exitAction)

        self.statusBar().showMessage("Ready")

        self.setWindowTitle('(주)내가고자라니주식컨설팅')
        self.setWindowIcon(QIcon('sim.jpg'))
        self.setGeometry(800,350,400,400)
        

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('이건 <b>창닫아버리기</b> 버튼')

        btn = QPushButton("끄기", self)
        btn.setToolTip('이건 <b>창닫기</b> 버튼')
        btn.move(300, -1)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
