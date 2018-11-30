import unittest
from model import Model


class TestModel(unittest.TestCase):
    # 초기 설정!

    def setUp(self):
        self.g1 = Model('default')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
