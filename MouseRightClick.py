from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QLabel, QComboBox
from PyQt5.QtWidgets import QToolButton, QPushButton, QGroupBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QSizePolicy
from PyQt5 import QtGui, QtCore


class Button(QToolButton):

    def __init__(self, text, row, column, callback):
        super().__init__()
        self.row = row
        self.column = column
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.callback = callback

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 10)
        size.setWidth(max(size.width(), size.height()))
        return size

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.callback(self, 0)
            print("You click the LeftButton" , self)
        elif event.button() == Qt.RightButton:
            self.callback(self, 1)
            #Game.mineButtonRightClicked(self)
            print("You click the RightButton", self)





class Game(QWidget):

    def __init__(self, size, parent=None):
        super().__init__(parent)
        self.size = size
        self.mineButtons = [['0' for i in range(self.size)] for j in range(self.size)]
        self.initUI()

    '''
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print("You click the LeftButton!")

        elif QMouseEvent.button() == Qt.RightButton:
            print("You click the RightButton!")
    '''

    def initUI(self):
        optionLayout = QGridLayout()
        optionGroup = QGroupBox("Game Options")
        self.optionLabel = QLabel("Select the number of mines : ")
        self.optionBox = QComboBox()
        self.optionBox.addItems(list(map(str, range(1, self.size**2))))
        self.optionBox.setCurrentIndex(self.size-1)
        self.optionButton = QPushButton("Select")
        self.optionButton.clicked.connect(self.optionButtonClicked)
        optionLayout.addWidget(self.optionLabel, 0, 0)
        optionLayout.addWidget(self.optionBox, 0, 1)
        optionLayout.addWidget(self.optionButton, 0, 2)
        optionGroup.setLayout(optionLayout)

        mineLayout = QGridLayout()
        mineGroup = QGroupBox("Game Main")
        i = 0
        j = 0
        for button in range(self.size**2):
            self.mineButtons[i][j] = Button(' ', row=i, column=j, self.mineButtonClicked)
            mineLayout.addWidget(self.mineButtons[i][j], i, j)
            j += 1
            if j == self.size:
                i += 1
                j = 0
        mineGroup.setLayout(mineLayout)

        statusLayout = QGridLayout()
        # 클릭한 버튼 개수
        # 남은 버튼 개수
        #
        statusGroup = QGroupBox("Game Status")

        mainLayout = QGridLayout()
        mainLayout.addWidget(optionGroup, 0, 0)
        mainLayout.addWidget(mineGroup, 1, 0)
        mainLayout.addWidget(statusGroup, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("MineSweeper")
        self.show()

        self.mineButtons[1][1].


    def mineButtonClicked(self, button, status=0):
        if status:
            button.setText('!')
        else:
            button.setText('?')
            button.setEnabled(False)


    def optionButtonClicked(self):
        self.optionBox.setEnabled(False)
        self.optionButton.setEnabled(False)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = Game(10)
    game.show()
    sys.exit(app.exec_())

'''
class MyWidget(QWidget):


    def __init__(self):
        super(MyWidget, self).__init__()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print("Left Button Clicked")
        elif QMouseEvent.button() == Qt.RightButton:
            #do what you want here
            print("Right Button Clicked")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec_())
'''