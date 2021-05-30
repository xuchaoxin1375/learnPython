import sys
from datetime import datetime

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

        # Row colors empty by default.
        self._row_colors = {}

    def data(self, index, role):
        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, bool):
                if value:
                    return QtGui.QIcon("tick.png")

                return QtGui.QIcon("cross.png")

        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")

            return value

        if role == Qt.BackgroundRole:
            color = self._row_colors.get(index.row())  # returns None if not in.
            if color:
                return QtGui.QColor(color)

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    def set_row_color(self, row, color):
        self._row_colors[row] = color


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = [
            [True, 9, 2],
            [1, 0, -1],
            [3, 5, False],
            [3, 3, 2],
            [datetime(2019, 5, 4), 8, 9],
        ]

        self.model = TableModel(data)
        self.model.set_row_color(1, '#b2182b')
        self.model.set_row_color(3, '#92c5de')
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
        self.setGeometry(600, 100, 400, 200)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
