from observable import Observable
import random

class Model(Observable):

    def __init__(self):
        Observable.__init__(self)

        # Initialize instance variables
        self.size = 0
        self.mine = []
        self.current = []
        self.unknowns = 0
        self.finished = False
        self.mineNumbers = 0


    def setArray(self, size, mineNumbers):
        # Make a new array and Locate mines at random index
        self.finished = False
        self.size = size
        self.unknowns = self.size ** 2
        self.mineNumbers = mineNumbers
        self.mine = [[0 for x in range(size+2)] for y in range(size+2)]
        self.current = [['_' for x in range(size+2)] for y in range(size+2)]
        for n in range(mineNumbers):
            i = random.randrange(1, self.size+1)
            j = random.randrange(1, self.size+1)
            while self.mine[i][j] != 0:
                i = random.randrange(1, self.size+1)
                j = random.randrange(1, self.size+1)
            self.mine[i][j] = "*"
        # Calculate and set counts next to bomb.
        self.setCount()


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
        # 모든 칸을 순회하되, 지뢰인 경우 8방위에 대해 더할 것인지.


        '''
        row = 1
        column = 1
        while row <= self.size:
            if self.mine[row][column] != '*':
                self.addCount2(row, column, row - 1, column - 1)
                self.addCount2(row, column, row - 1, column)
                self.addCount2(row, column, row - 1, column + 1)
                self.addCount2(row, column, row, column - 1)
                self.addCount2(row, column, row, column + 1)
                self.addCount2(row, column, row + 1, column - 1)
                self.addCount2(row, column, row + 1, column)
                self.addCount2(row, column, row + 1, column + 1)
        column += 1
        if column >= self.size + 1:
            row += 1
            column = 1
        # 모든 칸에서 8방위에 대해 검사하여 지뢰가 있으면 각각을 카운트할 것인지
        '''

    def addCount(self, row, column):
        if self.mine[row][column] != '*':
            self.mine[row][column] += 1

    '''
    def addCount2(self, row, column, r, c):
        if self.mine[r][c] == '*':
            self.mine[row][column] += 1
    '''

    def guess(self, row, column, parent=None):
        # out of range 처리
        if (not(0 < row <= self.size)) or (not(0 < column <= self.size)):
            return True

        # 이미 와봤던 지역
        if self.current[row][column] == ' ':
            return True

        # 지뢰 발견
        if self.mine[row][column] == '*':
            print(self.current)
            print(self.mine)
            self.current = [['*' if self.mine[x][y] == '*' else ' ' for x in range(self.size+2)] for y in range(self.size+2)]
            self.notifyAnswer(False)
            self.notifyStatus(0)
            self.finished = True
            return False

        # 다 찾았을 때
        if self.unknowns == self.size ** 2 - self.mineNumbers:
            self.current = [['x' if self.mine[x][y] == '*' else ' ' for x in range(self.size + 2)] for y in
                            range(self.size + 2)]
            self.notifyAnswer(True)
            self.notifyStatus(self.unknowns)
            self.finished = True
            return True

        self.unknowns -= 1

        # 지뢰 인접 구역 발견
        if self.mine[row][column] > 0:
            self.current[row][column] = self.mine[row][column]
            self.notifyMine(row, column, self.current[row][column])
            self.notifyStatus(self.unknowns)
            return True

        # 황무지 발견
        self.current[row][column] = ' '
        self.notifyMine(row, column, self.current[row][column])
        self.notifyStatus(self.unknowns)

        # 재귀적으로 호출
        if parent == 'left':
            return \
                self.guess(row, column - 1, 'left') and\
                self.guess(row - 1, column, 'down') and\
                self.guess(row + 1, column, 'up')
        if parent == 'right':
            return \
                self.guess(row, column + 1, 'right') and\
                self.guess(row - 1, column, 'down') and\
                self.guess(row + 1, column, 'up')
        if parent == 'down':
            return \
                self.guess(row, column - 1, 'left') and\
                self.guess(row, column + 1, 'right') and\
                self.guess(row - 1, column, 'down')
        if parent == 'up':
            return \
                self.guess(row, column - 1, 'left') and\
                self.guess(row, column + 1, 'right') and\
                self.guess(row + 1, column, 'up')
        return \
            self.guess(row, column - 1, 'left') and\
            self.guess(row, column + 1, 'right') and\
            self.guess(row - 1, column, 'down') and\
            self.guess(row + 1, column, 'up')

    def setStatus(self, finished):
        self.finished = finished
        self.notifyAnswer(False)

    def notifyAnswer(self, foundAnswer):
        if foundAnswer:
            for row in range(1, self.size + 1):
                for column in range(1, self.size + 1):
                    self.notifyMine(row, column, self.current[row][column])
        else:
            for row in range(1, self.size + 1):
                for column in range(1, self.size + 1):
                    self.notifyMine(row, column, self.current[row][column])

    def notifyMine(self, row, column, value):
        for observer in self.observers:
            observer.updateMine(row-1, column-1, value)

    def notifyStatus(self, unknowns):
        for observer in self.observers:
            observer.updateStatus(unknowns)