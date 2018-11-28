import sys

from PyQt5.QtWidgets import QApplication
from view import View
from model import Model
from controller import Controller

class MineSweeper(QApplication):
    def __init__(self, sys_argv):
        super(__class__, self).__init__(sys_argv)

        self.model = Model(10, 20)
        self.controller = Controller(self.model)
        self.view = View(self.controller)
        self.model.register(self.view)
        self.view.show()


if __name__ == '__main__':
    app = MineSweeper(sys.argv)
    sys.exit(app.exec_())