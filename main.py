import sys
from random import randint

from Ui import Ui_MainWindow
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.create_circle)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        r = randint(0, 250)
        qp.drawEllipse(randint(0, 600 - r), randint(0, 600 - r), r, r)
        self.do_paint = False

    def create_circle(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())