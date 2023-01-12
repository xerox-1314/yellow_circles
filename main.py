import sys
from ui_file import Ui_MainWindow

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class YellowGeneration(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Git и желтые окружности')
        self.but.clicked.connect(self.paint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        x = randint(1, self.width() - 1)
        y = randint(1, self.height() - 1)
        r = randint(1, min([self.height() - y, self.width() - x]))
        qp.drawEllipse(x, y, r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = YellowGeneration()
    main_app.show()
    sys.excepthook = except_hook

    sys.exit(app.exec_())
