import unittest
from view import View
from observer import Observer


class TestView(unittest.TestCase):
    # 초기 설정!
    def setUp(self):
        self.g1 = View(Observer)

    def tearDown(self):
        pass

    def reStartTest(self):
        reStartg2 = self.g1.reStartGame()
        self.assertNotEqual(self.g1, reStartg2)


if __name__ == '__main__':
    unittest.main()
