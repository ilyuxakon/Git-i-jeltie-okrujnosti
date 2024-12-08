from os import name
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic

from random import randrange


class JeltieOkrujnosti(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.flag = False
        self.ellipse = list()
        self.pushButton.clicked.connect(self.creater_painter)

    def creater_painter(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        if self.flag:
            self.draw(painter)
        painter.end()

    def draw(self, painter):
        painter.setBrush(QColor('yellow'))
        x, y, r = randrange(0, 490), randrange(0, 490), randrange(1, 100)
        self.ellipse.append((x, y, r))
        for i in self.ellipse:
            painter.drawEllipse(i[0], i[1], i[2], i[2])

        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = JeltieOkrujnosti()
    x.show()
    sys.exit(app.exec())