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
        self.optionLayout = QGridLayout()
        self.optionGroup = QGroupBox("Mine Options")
        self.optionLabel = QLabel("Select the number of mines : ")
        self.optionBox = QComboBox()
        self.optionBox.addItems(list(map(str, range(1, self.size**2))))
        self.optionBox.setCurrentIndex(3*(self.size-1))
        self.optionButton = QPushButton("Start")
        self.optionButton.clicked.connect(self.optionButtonClicked)
        self.optionLayout.addWidget(self.optionLabel, 0, 0)
        self.optionLayout.addWidget(self.optionBox, 0, 1)
        self.optionLayout.addWidget(self.optionButton, 0, 2)
        self.optionGroup.setLayout(self.optionLayout)

        self.selectedLayout = QGridLayout()
        self.selectedGroup = QGroupBox("Total Mines")
        self.selectedLabel = QLabel()
        self.selectedLabel.setAlignment(Qt.AlignCenter)
        self.selectedLabel.font().setPointSize(self.selectedLabel.font().pointSize() + 10)
        self.selectedLayout.addWidget(self.selectedLabel, 0, 0)
        self.selectedGroup.setLayout(self.selectedLayout)

        self.mineLayout = QGridLayout()
        self.mineGroup = QGroupBox("Game Main")
        self.mineGroup.setEnabled(False)
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

        self.statusLayout = QGridLayout()
        self.statusGroup = QGroupBox("Game Status")
        self.arrayDisplay = QLabel("Array size : ")
        self.arrayLabel = QLabel(str(self.size)+"x"+str(self.size))
        self.unknownDisplay = QLabel("Unknown areas : ")
        self.unknowns = self.size ** 2
        self.unknownLabel = QLabel(str(self.unknowns))
        self.flagDisplay = QLabel("Flag areas : ")
        self.flags = 0
        self.flagLabel = QLabel(str(self.flags))
        self.statusLayout.addWidget(self.arrayDisplay, 0, 0)
        self.statusLayout.addWidget(self.arrayLabel, 0, 1)
        self.statusLayout.addWidget(self.unknownDisplay, 1, 0)
        self.statusLayout.addWidget(self.unknownLabel, 1, 1)
        self.statusLayout.addWidget(self.flagDisplay, 2, 0)
        self.statusLayout.addWidget(self.flagLabel, 2, 1)
        self.statusGroup.setLayout(self.statusLayout)

        self.menuLayout = QGridLayout()
        self.menuGroup = QGroupBox("Game menu")
        self.exitButton = QPushButton("Exit")
        self.restartButton = QPushButton("Restart")
        self.newGameButton = QPushButton("New Game")
        self.giveUpButton = QPushButton("Give up game")
        self.menuLayout.addWidget(self.giveUpButton, 0, 0)
        self.menuLayout.addWidget(self.restartButton, 0, 1)
        self.menuLayout.addWidget(self.newGameButton, 0, 2)
        self.menuLayout.addWidget(self.exitButton, 0, 3)
        self.menuGroup.setLayout(self.menuLayout)

        self.exitButton.clicked.connect(self.menuButtonClicked)
        self.restartButton.clicked.connect(self.menuButtonClicked)
        self.newGameButton.clicked.connect(self.menuButtonClicked)
        self.giveUpButton.clicked.connect(self.menuButtonClicked)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.optionGroup, 0, 0)
        self.mainLayout.addWidget(self.selectedGroup, 0, 1)
        self.mainLayout.addWidget(self.mineGroup, 1, 0)
        self.mainLayout.addWidget(self.statusGroup, 1, 1)
        self.mainLayout.addWidget(self.menuGroup, 2, 0, 1, 2)

        self.setLayout(self.mainLayout)
        self.setWindowTitle("MineSweeper")
        self.show()
        '''
    def delUI(self):
        self.optionGroup.close()
        self.menuGroup.close()
        self.selectedGroup.close()
        self.statusGroup.close()
        self.mineGroup.close()
        self.close()

        #self.optionButton.close()
        #self.optionLabel.close()
        #self.optionBox.close()
        #self.exitButton.close()


        #for i in range(self.optionLayout.count()): self.optionLayout.itemAt(i).widget().close()
        '''

    def reStart(self):
        self.optionGroup.setEnabled(True)
        self.mineGroup.setEnabled(False)
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

    def giveUp(self):
        # 버튼 정답을 다 알려주는 코드 작성 (미완성)
        self.optionGroup.setEnabled(True)
        self.mineGroup.setEnabled(False)

    def mineButtonClicked(self, button):
        if button.status == 0:
            self.unknowns -= 1
            button.setStyleSheet('color: rgb(0, 0, 0)')
            self.controller.guessArea(button.row, button.column)


        elif button.status == 1:
            if int(self.mineNumber) - self.flags > 0:  # 깃발 개수는 최대 폭탄 개수를 넘길 수 없음
                self.unknowns -= 1
                self.flags += 1
                button.setText('✖')
                button.setStyleSheet('color: rgb(255, 0, 0)')
        else:
            if button.text() == '✖':
                self.flags -= 1
                self.unknowns += 1
                button.status = 0
                button.setText('')
                button.setStyleSheet('color: rgb(0, 0, 0)')

        # 최대 폭탄 개수가 5개라면, 깃발 5개를 꽂으면 더이상 우클릭으로 깃발을 만들지 않음.
        # 그런 상태에서 좌클릭으로 popzero를 터트리면, Total Mines 값이 최대 폭탄 값으로 돌아가야하는데
        # 여전히 0이라서 우클릭으로 깃발을 꽂지 못하는 버그 발생
        # 해당 버그는 popzero가 터트렸을 때, unknowns 값이 1만 감소하는 것을 보면 이해하기 쉬울 것 같음.
        # 아마 해결 방안도 똑같거나 비슷하다고 생각함.
        # flags, unknowns 값을 update에서 수정해주면 좋을 것 같은데.. 뷰 자체에 구현을 해봤지만 의미 없었음
        # flags, unknowns 값을 update로 수정하려면 변수들을 모델로 이동 + 로직 추가 ...
        self.selectedLabel.setText(str(int(self.mineNumber) - self.flags))  # Total Mines 값은 (폭탄 개수 - 깃발 꽂은 개수)
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
            self.giveUp()
        elif self.sender() == self.restartButton:
            self.reStart()
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


    def update(self, row, column, value, mineNumbers):
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
            self.mineButtons[row][column].setStyleSheet("background-color: gray") #버튼 배경 색
            self.mineButtons[row][column].setEnabled(False)

        self.mineNumber = mineNumbers



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = View()
    game.show()
    sys.exit(app.exec_())

