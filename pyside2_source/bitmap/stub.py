import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)  # <1>
        canvas.fill(Qt.white)  # <2>

        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        pass


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
