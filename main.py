from os import name
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor

from random import randrange

from UI import Ui_MainWindow


class JeltieOkrujnosti(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        color = QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256))
        x, y, r = randrange(0, 490), randrange(0, 490), randrange(1, 100)
        self.ellipse.append((x, y, r, color))
        for i in self.ellipse:
            painter.setBrush(i[3])
            painter.drawEllipse(i[0], i[1], i[2], i[2])

        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = JeltieOkrujnosti()
    x.show()
    sys.exit(app.exec())