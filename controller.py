class Controller:

    def __init__(self, model):
        self.model = model

    def notifyArray(self, size, mineNumber):
        self.model.setArray(size, mineNumber)

    def guessArea(self, row, column):
        return self.model.guess(row+1, column+1)

    def getCurrentStatus(self, finished=False):
        return self.model.getStatus(finished)

    def restartGame(self):
        self.model.__init__()
        self.notifyArray()
