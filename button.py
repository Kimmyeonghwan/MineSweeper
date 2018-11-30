from PyQt5.QtWidgets import QToolButton, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


class Button(QToolButton):

    def __init__(self, text, row, column, status, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

        self.row = row
        self.column = column
        self.status = status
        self.callback = callback
        font = self.font()
        font.setPointSize(font.pointSize()+5)
        self.setFixedSize(self.sizeHint())


    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 15)
        size.setWidth(max(size.width(), size.height()))
        return size


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.status = 0
            self.callback(self)
        elif event.button() == Qt.RightButton:
            self.status += 1
            self.callback(self)