from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QLabel, QComboBox
from PyQt5.QtWidgets import QToolButton, QPushButton, QGroupBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QSizePolicy

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 10)
        size.setWidth(max(size.width(), size.height()))
        return size


class Game(QWidget):

    def __init__(self, size, parent=None):
        super().__init__(parent)
        self.size = size
        self.mineButtons = [['0' for i in range(self.size)] for j in range(self.size)]
        self.initUI()

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
            self.mineButtons[i][j] = Button(' ', self.mineButtonClicked)
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

    def mineButtonClicked(self):
        sender = self.sender()
        sender.setText('1')
        sender.setEnabled(False)

    def optionButtonClicked(self):
        self.optionBox.setEnabled(False)
        self.optionButton.setEnabled(False)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = Game(10)
    game.show()
    sys.exit(app.exec_())

