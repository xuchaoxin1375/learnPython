import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton  # <1>


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # <2>

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_click)
        button.clicked.connect(self.the_button_was_toggled)
        button.clicked.connect(self.the_button_was_toggled_explorer)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")
    def the_button_was_click(self):
        print("Click!")
    def the_button_was_toggled(self, checked):
        # print
        print("Checked?", checked)
    def the_button_was_toggled_explorer(self,explorer):
        print("Clicked!:type judge with number",explorer+5)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
