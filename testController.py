import unittest
from controller import Controller


class TestController(unittest.TestCase):
    # 초기 설정!
    def setUp(self):
        self.g1 = Controller('default')

    def tearDown(self):
        pass

    def Test(self):
        self.g1.notifyArray(8, 5)
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
