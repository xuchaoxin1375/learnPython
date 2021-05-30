import sys

from PySide2.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QPushButton, QWidget


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        lineEdit = QLineEdit()
        button = QPushButton("Clear")
        layout = QHBoxLayout()
        layout.addWidget(lineEdit)
        layout.addWidget(button)

        button.pressed.connect(lineEdit.clear)

        self.setLayout(layout)
        self.setWindowTitle("Why?")
        self.show()


app = QApplication(sys.argv)
window = MyWindow()
app.exec_()
