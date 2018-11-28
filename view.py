from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QLabel, QComboBox
from PyQt5.QtWidgets import QToolButton, QPushButton, QGroupBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QSizePolicy
from button import Button
from observer import Observer


class View(Observer, QWidget):

    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setSize()
        self.mineButtons = [['' for i in range(self.size)] for j in range(self.size)]
        self.initUI()


    def initUI(self):
        optionLayout = QGridLayout()
        self.optionGroup = QGroupBox("Mine Options")
        self.optionLabel = QLabel("Select the number of mines : ")
        self.optionBox = QComboBox()
        self.optionBox.addItems(list(map(str, range(1, self.size**2))))
        self.optionBox.setCurrentIndex(3*(self.size-1))
        self.optionButton = QPushButton("Start")
        self.optionButton.clicked.connect(self.optionButtonClicked)
        optionLayout.addWidget(self.optionLabel, 0, 0)
        optionLayout.addWidget(self.optionBox, 0, 1)
        optionLayout.addWidget(self.optionButton, 0, 2)
        self.optionGroup.setLayout(optionLayout)

        selectedLayout = QGridLayout()
        self.selectedGroup = QGroupBox("Total Mines")
        self.selectedLabel = QLabel()
        self.selectedLabel.setAlignment(Qt.AlignCenter)
        self.selectedLabel.font().setPointSize(self.selectedLabel.font().pointSize() + 10)
        selectedLayout.addWidget(self.selectedLabel, 0, 0)
        self.selectedGroup.setLayout(selectedLayout)

        mineLayout = QGridLayout()
        self.mineGroup = QGroupBox("Game Main")
        self.mineGroup.setEnabled(False)
        i = 0
        j = 0
        for button in range(self.size**2):
            self.mineButtons[i][j] = Button('', i, j, 0, self.mineButtonClicked)
            mineLayout.addWidget(self.mineButtons[i][j], i, j)
            j += 1
            if j == self.size:
                i += 1
                j = 0
        self.mineGroup.setLayout(mineLayout)

        statusLayout = QGridLayout()
        self.statusGroup = QGroupBox("Game Status")
        self.arrayDisplay = QLabel("Array size : ")
        self.arrayLabel = QLabel(str(self.size)+"x"+str(self.size))
        self.unknownDisplay = QLabel("Unknown areas : ")
        self.unknowns = self.size ** 2
        self.unknownLabel = QLabel(str(self.unknowns))
        self.flagDisplay = QLabel("Flag areas : ")
        self.flags = 0
        self.flagLabel = QLabel(str(self.flags))
        statusLayout.addWidget(self.arrayDisplay, 0, 0)
        statusLayout.addWidget(self.arrayLabel, 0, 1)
        statusLayout.addWidget(self.unknownDisplay, 1, 0)
        statusLayout.addWidget(self.unknownLabel, 1, 1)
        statusLayout.addWidget(self.flagDisplay, 2, 0)
        statusLayout.addWidget(self.flagLabel, 2, 1)
        self.statusGroup.setLayout(statusLayout)

        menuLayout = QGridLayout()
        self.menuGroup = QGroupBox("Game menu")
        self.exitButton = QPushButton("Exit")
        self.restartButton = QPushButton("Restart")
        self.newGameButton = QPushButton("New Game")
        self.giveUpButton = QPushButton("Give up game")
        menuLayout.addWidget(self.giveUpButton, 0, 0)
        menuLayout.addWidget(self.restartButton, 0, 1)
        menuLayout.addWidget(self.newGameButton, 0, 2)
        menuLayout.addWidget(self.exitButton, 0, 3)
        self.menuGroup.setLayout(menuLayout)

        self.exitButton.clicked.connect(self.menuButtonClicked)
        self.restartButton.clicked.connect(self.menuButtonClicked)
        self.newGameButton.clicked.connect(self.menuButtonClicked)
        self.giveUpButton.clicked.connect(self.menuButtonClicked)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.optionGroup, 0, 0)
        mainLayout.addWidget(self.selectedGroup, 0, 1)
        mainLayout.addWidget(self.mineGroup, 1, 0)
        mainLayout.addWidget(self.statusGroup, 1, 1)
        mainLayout.addWidget(self.menuGroup, 2, 0, 1, 2)

        self.setLayout(mainLayout)
        self.setWindowTitle("MineSweeper")
        self.show()

    def mineButtonClicked(self, button):
        if button.status == 0:
            button.setStyleSheet('color: rgb(0, 0, 0)')
            self.unknowns -= 1
            self.controller.guessArea(button.row, button.column)
        elif button.status == 1:
            button.setText('✖')
            self.flags += 1
            self.unknowns -= 1
            button.setStyleSheet('color: rgb(255, 0, 0)')
        else:
            button.status = 0
            button.setText('')
            self.flags -= 1
            self.unknowns += 1
            button.setStyleSheet('color: rgb(0, 0, 0)')
        self.flagLabel.setText(str(self.flags))
        self.unknownLabel.setText(str(self.unknowns))


    def optionButtonClicked(self):
        self.optionGroup.setEnabled(False)
        self.mineGroup.setEnabled(True)
        self.mineNumber = self.optionBox.currentText()
        self.selectedLabel.setText(self.mineNumber)
        self.selectedLabel.setStyleSheet('color: rgb(0, 0, 255)')

        self.controller.notifyArray(self.size, self.mineNumber)


    def menuButtonClicked(self):
        if self.sender() == self.exitButton:
            self.close()
        elif self.sender() == self.giveUpButton:
            pass
        elif self.sender() == self.restartButton:
            self.initUI()
        elif self.sender() == self.newGameButton:
            if self.close(): self.__init__(self.controller)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Notice", "Are you sure to quit?",
                QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def setSize(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Welcome to MineSweeper Game")
        msgBox.setText("Select a game level you want to enjoy")
        msgBox.addButton(QPushButton('Hard(16x16)'), QMessageBox.RejectRole)
        msgBox.addButton(QPushButton('Normal(12x12)'), QMessageBox.NoRole)
        msgBox.addButton(QPushButton('Easy(8x8)'), QMessageBox.YesRole)
        self.level = msgBox.exec_()
        self.size = (8 if self.level == 2 else (12 if self.level == 1 else 16))

    def update(self, row, column, value):
        if value == -1:
            i = 0
            j = 0
            for button in range(self.size ** 2):
                self.mineButtons[i][j].setText('x')
                self.mineButtons[i][j].setStyleSheet('color: rgb(0, 0, 0)')
                self.mineButtons[i][j].setEnabled(False)
                j += 1
                if j == self.size:
                    i += 1
                    j = 0
        else:
            if type(value) != int:
                self.mineButtons[row][column].setText('0')
            elif value == 1:
                self.mineButtons[row][column].setStyleSheet('color: rgb(0, 0, 150)')
                self.mineButtons[row][column].setText(str(value))
            elif value == 2:
                self.mineButtons[row][column].setStyleSheet('color: rgb(0, 150, 0)')
                self.mineButtons[row][column].setText(str(value))
            elif value == 3:
                self.mineButtons[row][column].setStyleSheet('color: rgb(150, 0, 0)')
                self.mineButtons[row][column].setText(str(value))
            elif value >= 4:
                self.mineButtons[row][column].setStyleSheet('color: rgb(150, 150, 0)')
            self.mineButtons[row][column].setText(str(value))
            self.mineButtons[row][column].setEnabled(False)




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = View(10)
    game.show()
    sys.exit(app.exec_())

