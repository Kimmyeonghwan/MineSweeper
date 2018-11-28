from PyQt5.QtWidgets import QToolButton, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)
        self.callback = callback

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 10)
        size.setWidth(max(size.width(), size.height()))
        return size

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.status = 0
        elif event.button() == Qt.RightButton:
            self.status = 1
        return QWidget.mousePressEvent(self, event)