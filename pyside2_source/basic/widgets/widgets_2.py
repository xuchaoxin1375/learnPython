import sys

from PySide2.QtGui import QPixmap
from PySide2.QtW idgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        widget.setPixmap(QPixmap("otje.jpg"))
        widget.setScaledContents(True) dd

        self.setCentralWidg et(widget)


app = QApplication(sys.argv)

window = MainWindow();
window.show()

app.exec_()
