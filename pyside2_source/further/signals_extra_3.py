import sys

from PySide2.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        v = QVBoxLayout()
        h = QHBoxLayout()

        # tag::loop[]
        for a in range(10):
            button = QPushButton(str(a))
            button.clicked.connect(lambda checked=False, a=a: self.button_clicked(a))  # <1>
            h.addWidget(button)
        # end::loop[]

        v.addLayout(h)
        self.label = QLabel("")
        v.addWidget(self.label)

        w = QWidget()
        w.setLayout(v)
        self.setCentralWidget(w)

    def button_clicked(self, n):
        self.label.setText(str(n))


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
