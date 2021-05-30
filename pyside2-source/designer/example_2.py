import sys

from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader

loader = QUiLoader()


def mainwindow_setup(w):
    w.setWindowTitle("MainWindow Title")


app = QtWidgets.QApplication(sys.argv)
window = loader.load("mainwindow.ui", None)
mainwindow_setup(window)
window.show()
app.exec_()
