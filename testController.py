import unittest
from controller import Controller
from model import Model


class TestController(unittest.TestCase):
    # 초기 설정!
    def setUp(self):
        self.g1 = Controller(Model)

    def tearDown(self):
        pass

        # 컨트롤러는.. 뭘 테스트 해야하지..? notifly? update???
        '''
    def test(self):
        self.g1.notifyArray(8, 5)
        self.assertEqual()
        '''

    def test2(self):
        pass


if __name__ == '__main__':
    unittest.main()
