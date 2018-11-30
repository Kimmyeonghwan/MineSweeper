import unittest
from view import View
from observer import Observer


class TestView(unittest.TestCase):

    def setUp(self):
        self.g1 = View(Observer)

    def tearDown(self):
        pass

    # GUI는 테스트가 안되는 것 같아요 !!!!!!!!!!!
    '''
    def testMineButtonClicked(self):
        self.g1.mineButtons[0][0].status = 0
        self.assertEqual(self.g1.mineButtons[0][0], ' ')
        '''



if __name__ == '__main__':
    unittest.main()