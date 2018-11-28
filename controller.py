class Controller:

    def __init__(self, model):
        self.model = model

    def guess_area(self, row, column):
        self.model.guess(row, column)

