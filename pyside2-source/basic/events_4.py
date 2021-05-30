import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QAction, QApplication, QLabel, QMainWindow, QMenu


# tag::MainWindow[]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec_(self.mapToGlobal(pos))


# end::MainWindow[]

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
