class Controller:

    def __init__(self, model):
        self.model = model

    def notifyArray(self, size, mineNumber):
        self.model.setArray(size, mineNumber)

    def guessArea(self, row, column):
        self.model.guess(row+1, column+1)