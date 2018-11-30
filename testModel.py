import unittest
from model import Model


class TestModel(unittest.TestCase):
    # 초기 설정!

    def setUp(self):
        self.g1 = Model()

        self.g1.unknowns = 5
        self.g1.mineNumbers = 0
        self.g1.answer = []

        self.g1.size = 8
        self.g1.mine = [[0 for x in range(self.g1.size + 2)] for y in range(self.g1.size + 2)]
        self.g1.current = [['_' for x in range(self.g1.size + 2)] for y in range(self.g1.size + 2)]
    def tearDown(self):
        pass

    # 이걸 굳이 해야하는 이유가 있나 ㅇㅅㅇ?
    def testSetArray(self):
        self.g1.setArray(8, 5)
        self.assertEqual(self.g1.mineNumbers, 5)
        self.assertEqual(self.g1.size, 8)

    def testGetStatus(self):
        self.assertFalse(self.g1.getStatus(False))
        self.assertTrue(self.g1.getStatus(True))

        self.g1.getStatus(True)
        self.assertEqual(self.g1.unknowns, 'GAME OVER')


        self.g1.getStatus(False)
        self.assertEqual(self.g1.unknowns, 64)

        self.g1.mineNumbers = self.g1.unknowns
        self.g1.getStatus(False)
        self.assertEqual(self.g1.unknowns, 'GAME CLEAR')

    def testGuess(self):
        self.assertTrue(self.g1.guess(9, 1))
        self.assertTrue(self.g1.guess(0, 1))

        self.g1.mine[1][1] = ' '
        self.g1.mine[2][1] = '*'

        self.assertTrue(self.g1.guess(1, 1))
        self.assertFalse(self.g1.guess(2, 1))


if __name__ == '__main__':
    unittest.main()
