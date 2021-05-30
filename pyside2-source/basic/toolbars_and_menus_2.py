import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QAction, QApplication, QLabel, QMainWindow, QToolBar


# tag::MainWindow[]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        print("click", s)


# end::MainWindow[]


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
