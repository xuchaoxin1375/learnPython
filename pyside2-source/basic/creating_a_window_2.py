# tag::imports[]
from PySide2.QtWidgets import QApplication, QPushButton
# end::imports[]

import sys

# tag::QApplication[]
app = QApplication(sys.argv)
# end::MainWindow[]

# tag::QWidget[]
window = QPushButton("Push Me")
window.show()
# end::QWidget[]

# tag::exec[]
app.exec_()
# end::exec[]
