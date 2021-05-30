import sys

# tag::imports[]
from random import choice, randint  # <1>

# end::imports[]
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.setCentralWidget(self.label)
        self.draw_something()

    # tag::draw_something[]
    def draw_something(self):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for n in range(10000):
            painter.drawPoint(
                200 + randint(-100, 100), 150 + randint(-100, 100)  # x  # y
            )
        painter.end()

    # end::draw_something[]


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
