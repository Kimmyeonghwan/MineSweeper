from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QLabel, QComboBox
from PyQt5.QtWidgets import QToolButton, QPushButton, QGroupBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QFont
from button import Button
from observer import Observer


class View(Observer, QWidget):

    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.flags = 0

        self.setSize()
        self.mineButtons = [['' for i in range(self.size)] for j in range(self.size)]
        self.initUI()


    def initUI(self):
        # font size for label setting
        topFont = QFont()
        topFont.setPointSize(30)
        statusFont = QFont()
        statusFont.setPointSize(20)
        displayFont = QFont()
        displayFont.setPointSize(12)

        # Option layout setting
        optionLayout = QGridLayout()
        self.optionGroup = QGroupBox("Mine Options")
        self.optionLabel = QLabel("Select the number of mines : ")
        self.optionLabel.setFont(displayFont)
        self.optionBox = QComboBox()
        self.optionBox.addItems(list(map(str, range(1, self.size**2))))
        self.optionBox.setCurrentIndex(3*(self.size-1))
        self.optionButton = QPushButton("Start")
        self.optionButton.clicked.connect(self.optionButtonClicked)
        optionLayout.addWidget(self.optionLabel, 0, 0)
        optionLayout.addWidget(self.optionBox, 0, 1)
        optionLayout.addWidget(self.optionButton, 0, 2)
        self.optionGroup.setLayout(optionLayout)

        # Number of mines layout setting
        selectedLayout = QGridLayout()
        self.selectedGroup = QGroupBox("Total Mines")
        self.selectedLabel = QLabel()
        self.selectedLabel.setAlignment(Qt.AlignCenter)
        self.selectedLabel.setFont(topFont)
        selectedLayout.addWidget(self.selectedLabel, 0, 0)
        self.selectedGroup.setLayout(selectedLayout)

        # Mine button layout setting
        self.mineLayout = QGridLayout()
        self.mineGroup = QGroupBox("Game Main")
        self.mineGroup.setEnabled(False)
        row = 0
        column = 0
        for button in range(self.size**2):
            self.mineButtons[row][column] = Button('', row, column, 0, self.mineButtonClicked)
            self.mineLayout.addWidget(self.mineButtons[row][column], row, column)
            column += 1
            if column == self.size:
                row += 1
                column = 0
        self.mineGroup.setLayout(self.mineLayout)

        # current game status setting
        statusLayout = QGridLayout()
        self.statusGroup = QGroupBox("Game Status")
        self.arrayDisplay = QLabel("Array size : ")
        self.arrayDisplay.setFont(displayFont)
        self.arrayLabel = QLabel(str(self.size)+"x"+str(self.size))
        self.arrayLabel.setFont(statusFont)
        self.unknownDisplay = QLabel("Unknown areas : ")
        self.unknownDisplay.setFont(displayFont)
        self.unknownLabel = QLabel(str(self.size**2))
        self.unknownLabel.setFont(statusFont)
        self.flagDisplay = QLabel("Flag areas : ")
        self.flagDisplay.setFont(displayFont)
        self.flagLabel = QLabel(str(self.flags))
        self.flagLabel.setFont(statusFont)
        statusLayout.addWidget(self.arrayDisplay, 0, 0)
        statusLayout.addWidget(self.arrayLabel, 0, 1)
        statusLayout.addWidget(self.unknownDisplay, 1, 0)
        statusLayout.addWidget(self.unknownLabel, 1, 1)
        statusLayout.addWidget(self.flagDisplay, 2, 0)
        statusLayout.addWidget(self.flagLabel, 2, 1)
        self.statusGroup.setLayout(statusLayout)

        # game menu layout setting
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

        # main layout setting
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.optionGroup, 0, 0)
        mainLayout.addWidget(self.selectedGroup, 0, 1)
        mainLayout.addWidget(self.mineGroup, 1, 0)
        mainLayout.addWidget(self.statusGroup, 1, 1)
        mainLayout.addWidget(self.menuGroup, 2, 0, 1, 2)
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        self.setLayout(mainLayout)
        self.setWindowTitle("MineSweeper")
        self.show()


    def reStartGame(self):
        # initialize game ui
        self.optionGroup.setEnabled(True)
        self.mineGroup.setEnabled(False)
        self.unknownLabel.setText(str(self.size ** 2))
        self.unknownLabel.setStyleSheet('color: rgb(0, 0, 0)')
        self.flags = 0

        # re-compose buttons
        i = 0
        j = 0
        for button in range(self.size**2):
            self.mineButtons[i][j] = Button('', i, j, 0, self.mineButtonClicked)
            self.mineLayout.addWidget(self.mineButtons[i][j], i, j)
            j += 1
            if j == self.size:
                i += 1
                j = 0
        self.mineGroup.setLayout(self.mineLayout)


    def giveUpGame(self):
        self.controller.getCurrentStatus(True)
        self.optionGroup.setEnabled(False)
        self.mineGroup.setEnabled(False)

    def mineButtonClicked(self, button):
        if button.status == 0:
            button.setStyleSheet('color: rgb(0, 0, 0)')
            self.setButtonText(button, '')
            self.controller.guessArea(button.row, button.column)
            self.controller.getCurrentStatus()
        elif button.status == 1:
            if self.mineNumber - self.flags > 0:  # 깃발 개수는 최대 폭탄 개수를 넘길 수 없음
                self.flags += 1
                button.setText('✖')
                button.setStyleSheet('color: rgb(255, 0, 0)')
        else:
            self.setButtonText(button, '')
            button.setStyleSheet('color: rgb(0, 0, 0)')
        self.flagLabel.setText(str(self.flags))


    def optionButtonClicked(self):
        self.optionGroup.setEnabled(False)
        self.mineGroup.setEnabled(True)
        self.mineNumber = int(self.optionBox.currentText())
        self.selectedLabel.setText(str(self.mineNumber))
        self.selectedLabel.setStyleSheet('color: rgb(0, 0, 250)')
        self.controller.notifyArray(self.size, self.mineNumber)


    def menuButtonClicked(self):
        if self.sender() == self.exitButton:
            self.close()
        elif self.sender() == self.giveUpButton:
            self.giveUpGame()
        elif self.sender() == self.restartButton:
            self.reStartGame()
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


    def updateMine(self, row, column, value):
        if type(value) == int:
            if value == -1:
                self.mineGroup.setEnabled(False)
                self.mineButtons[row][column].setText('☹')
                self.mineButtons[row][column].setStyleSheet('background-color: gray; color: rgb(250, 0, 0)')
            elif value == 0:
                self.mineGroup.setEnabled(False)
                self.mineButtons[row][column].setText('☺')
                self.mineButtons[row][column].setStyleSheet('background-color: gray; color: rgb(0, 250, 0)')
            else:
                if value == 1:
                    self.mineButtons[row][column].setStyleSheet("background-color: gray; color: rgb(0, 0, 250)")
                elif value == 2:
                    self.mineButtons[row][column].setStyleSheet("background-color: gray; color: rgb(0, 250, 0)")
                elif value == 3:
                    self.mineButtons[row][column].setStyleSheet("background-color: gray; color: rgb(250, 0, 0)")
                else:
                    self.mineButtons[row][column].setStyleSheet("background-color: gray; color: rgb(250, 250, 0)")
                self.setButtonText(self.mineButtons[row][column], str(value))
                self.mineButtons[row][column].setEnabled(False)
        else:
            self.mineButtons[row][column].setStyleSheet("background-color: gray")
            self.setButtonText(self.mineButtons[row][column], str(value))
            self.mineButtons[row][column].setEnabled(False)

    def updateStatus(self, unknowns):
        self.unknownLabel.setText(str(unknowns))
        if unknowns == 'GAME CLEAR':
            self.unknownLabel.setStyleSheet('color: rgb(100, 200, 100)')
        elif unknowns == 'GAME OVER':
            self.unknownLabel.setStyleSheet('color: rgb(200, 100, 100)')

    def setButtonText(self, button, content=''):
        if button.text() == '✖':
            self.flags -= 1
            button.status = 0
        button.setText(content)

