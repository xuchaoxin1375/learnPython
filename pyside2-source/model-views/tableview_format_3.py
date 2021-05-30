import sys
from datetime import datetime

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    # tag::data[]
    def data(self, index, role):
        if role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int) or isinstance(value, float):
                # Align right, vertical middle.
                return Qt.AlignVCenter | Qt.AlignRight

        # existing `if role == Qt.DisplayRole:` block hidden
        # hidden for clarity.
        # end::data[]

        if role == Qt.BackgroundRole and index.column() == 3:
            # See below for the data structure.
            return QtGui.QColor("blue")

        if role == Qt.DisplayRole:
            # Get the raw value
            value = self._data[index.row()][index.column()]

            # Perform per-type checks and render accordingly.
            if isinstance(value, datetime):
                # Render time to YYY-MM-DD.
                return value.strftime("%Y-%m-%d")

            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value

            if isinstance(value, str):
                # Render strings with quotes
                return '"%s"' % value

            # Default (anything not captured above: e.g. int)
            return value

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = [
            [4, 9, 2],
            [1, -1, "hello"],
            [3.023, 5, -5],
            [3, 3, datetime(2017, 10, 1)],
            [7.555, 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
        self.setGeometry(600, 100, 400, 200)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
