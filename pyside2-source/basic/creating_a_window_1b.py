# tag::imports[]
from PySide2.QtWidgets import QApplication, QWidget
# end::imports[]

import sys

# tag::QApplication[]
app = QApplication(sys.argv)
# end::QApplication[]

# tag::QWidget[]
window = QWidget()
window.show()
# end::QWidget[]

# tag::exec[]
app.exec_()
# end::exec[]
