from observable import Observable

class Model(Observable):

    def __init__(self, n, mines):
        Observable.__init__(self)
        self.size = n
        self.mine = [[0 for x in range(n+2)] for y in range(n+2)]
        self.current = [['_' for x in range(n+2)] for y in range(n+2)]
        self.setMine(mines)
        self.setCount()
        self.printMineStatus()


    def setMine(self, count):
        import random
        for n in range(count):
            i = random.randrange(1, self.size+1)
            j = random.randrange(1, self.size+1)
            while self.mine[i][j] != 0:
                i = random.randrange(1, self.size+1)
                j = random.randrange(1, self.size+1)
            self.mine[i][j] = "*"


    def setCount(self):
        row = 1
        column = 1
        while row <= self.size:
            if self.mine[row][column] == '*':
                self.addCount(row-1, column-1)
                self.addCount(row-1, column)
                self.addCount(row-1, column+1)
                self.addCount(row, column-1)
                self.addCount(row, column+1)
                self.addCount(row+1, column-1)
                self.addCount(row+1, column)
                self.addCount(row+1, column+1)
            column += 1
            if column >= self.size+1:
                row += 1
                column = 1


    def addCount(self, row, column):
        if self.mine[row][column] != '*':
            self.mine[row][column] += 1


    def guess(self, row, column, parent=None):
        # out of range 처리
        if (not(0 < row <= self.size)) or (not(0 < column <= self.size)):
            return

        # 지뢰 발견
        if self.mine[row][column] == '*':
            self.current = [['x' for x in range(self.size+2)] for y in range(self.size+2)]
            return

        # 지뢰 인접 구역 발견
        if self.mine[row][column] != 0:
            self.current[row][column] = self.mine[row][column]
            return

        # 황무지 발견
        self.mine[row][column] = ' ' #얘 왜?왜?왜얘왜왜왜?????
        self.current[row][column] = ' '
        self.notify()
        if parent == 'left':
            return (
                self.guess(row, column - 1, 'left'),
                self.guess(row - 1, column, 'down'),
                self.guess(row + 1, column, 'up'))
        if parent == 'right':
            return (
                self.guess(row, column + 1, 'right'),
                self.guess(row - 1, column, 'down'),
                self.guess(row + 1, column, 'up'))
        if parent == 'down':
            return (
                self.guess(row, column - 1, 'left'),
                self.guess(row, column + 1, 'right'),
                self.guess(row - 1, column, 'down'))
        if parent == 'up':
            return (
                self.guess(row, column - 1, 'left'),
                self.guess(row, column + 1, 'right'),
                self.guess(row + 1, column, 'up'))
        return (
            self.guess(row, column - 1, 'left'),
            self.guess(row, column + 1, 'right'),
            self.guess(row - 1, column, 'down'),
            self.guess(row + 1, column, 'up'))


    def printMineStatus(self):
        print("<<< Answer sheet >>>")
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                print(self.mine[i][j], end=' ')
            print()

    def printCurrentStatus(self):
        print("<<< Default sheet >>>")
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                print(self.current[i][j], end=' ')
            print()

    def register(self, object):



        '''
    def test_normal(self, row, column):
        self.mine[row-1][column-1] += 1
        self.mine[row-1][column] += 1
        self.mine[row-1][column+1] += 1
        self.mine[row][column-1] += 1
        self.mine[row][column+1] += 1
        self.mine[row+1][column-1] += 1
        self.mine[row+1][column] += 1
        self.mine[row+1][column+1] += 1
    '''


if __name__ == '__main__':
    minesweeper = Model(10, 10)
    print()
    minesweeper.printCurrentStatus()
    print()
    minesweeper.guess(2, 2)
    print("After guess :")
    minesweeper.printCurrentStatus()