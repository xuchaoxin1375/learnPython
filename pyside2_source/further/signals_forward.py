import sys

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QApplication, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    message = Signal(str)

    def __init__(self):
        super().__init__()

        self.message.connect(self.my_custom_fn)

        le = QLineEdit("Enter some text")
        le.textChanged.connect(self.message.emit)  # <1>

        self.setCentralWidget(le)

    def my_custom_fn(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
