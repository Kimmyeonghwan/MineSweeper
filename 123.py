from PyQt5.QtWidgets import QApplication,QPushButton,QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtWidgets, QtGui

import PyQt5.QtWidgets,PyQt5.QtCore,sys

class HoverButton(QPushButton):
    mouseHover = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
     QPushButton.__init__(self, parent)
     self.setMouseTracking(True)

    def enterEvent(self, event):
     self.mouseHover.emit(True)
     bmp = QIcon("1.png")
     self.setIcon(bmp)
     self.setIconSize(QSize(200,200))

    def leaveEvent(self, event):
     self.mouseHover.emit(False)
     bmp = QIcon("2.png")
     self.setIcon(bmp)
     self.setIconSize(QSize(200,200))

class cssden(QtWidgets.QMainWindow):
    def __init__(self):
     super().__init__()

     # self.mwidget = QMainWindow(self)
     self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

     self.setMouseTracking(True)

     self.setFixedSize(1400, 923)


     #Button
     self.mbutton = HoverButton(self)
     self.mbutton.setStyleSheet("background-color: rgb(30,30,30);" 
            "background-image: url('resources/twitter-logo.png');" 
            "border: 3px solid black;" 
            "background-position: center;"
            )
     self.mbutton.setGeometry(2,300,110,60)
     self.mbutton.clicked.connect(self.yaz)
     self.show()

    def yaz(self):
     print("button pressed")

app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: rgb(30,30,30);border: 2px solid rgb(20,20,20)}")

ex = cssden()
sys.exit(app.exec_())

