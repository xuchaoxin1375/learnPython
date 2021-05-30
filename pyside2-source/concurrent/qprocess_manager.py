import re
import sys
import uuid
from collections import namedtuple

from PySide2.QtCore import (
    QAbstractListModel,
    QObject,
    QProcess,
    QRect,
    QRunnable,
    Qt,
    QTimer,
    Signal,
    Slot,
)
from PySide2.QtGui import QBrush, QColor, QPen
from PySide2.QtWidgets import (
    QApplication,
    QListView,
    QMainWindow,
    QPlainTextEdit,
    QProgressBar,
    QPushButton,
    QStyledItemDelegate,
    QVBoxLayout,
    QWidget,
)

# tag::constants[]
STATUS_COLORS = {
    QProcess.NotRunning: "#b2df8a",
    QProcess.Starting: "#fdbf6f",
    QProcess.Running: "#33a02c",
}

STATES = {
    QProcess.NotRunning: "Not running",
    QProcess.Starting: "Starting...",
    QProcess.Running: "Running...",
}

DEFAULT_STATE = {"progress": 0, "status": QProcess.Starting}
# end::constants[]


parsers = namedtuple("parsers", "progress data")
no_parsers = parsers(None, None)

progress_re = re.compile("Total complete: (\d+)%", re.M)

# tag::parsers[]
def simple_percent_parser(output):
    """
    Matches lines using the progress_re regex, 
    returning a single integer for the % progress.
    """
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)


def extract_vars(l):
    """
    Extracts variables from lines, looking for lines
    containing an equals, and splitting into key=value.
    """
    data = {}
    for s in l.splitlines():
        if "=" in s:
            name, value = s.split("=")
            data[name] = value
    return data


# end::parsers[]

# tag::jobManager[]
class JobManager(QAbstractListModel):
    """
    Manager to handle active jobs and stdout, stderr
    and progress parsers.
    Also functions as a Qt data model for a view
    displaying progress for each process.
    """

    _jobs = {}
    _state = {}
    _parsers = {}

    status = Signal(str)
    result = Signal(str, object)

    def __init__(self):
        super().__init__()

        self.status_timer = QTimer()
        self.status_timer.setInterval(100)
        self.status_timer.timeout.connect(self.notify_status)
        self.status_timer.start()

    def notify_status(self):
        n_jobs = len(self._jobs)
        self.status.emit("{} jobs".format(n_jobs))

    def execute(self, command, arguments, parsers=no_parsers):
        """
        Execute a command by starting a new process.
        """

        job_id = uuid.uuid4().hex

        # By default, the signals do not have access to any information about
        # the process that sent it. So we use this constructor to annotate
        #  each signal with a job_id.

        def fwd_signal(target):
            return lambda *args: target(job_id, *args)

        self._parsers[job_id] = parsers

        # Set default status to waiting, 0 progress.
        self._state[job_id] = DEFAULT_STATE.copy()

        p = QProcess()
        p.readyReadStandardOutput.connect(fwd_signal(self.handle_output))
        p.readyReadStandardError.connect(fwd_signal(self.handle_output))
        p.stateChanged.connect(fwd_signal(self.handle_state))
        p.finished.connect(fwd_signal(self.done))

        self._jobs[job_id] = p

        p.start(command, arguments)

        self.layoutChanged.emit()

    def handle_output(self, job_id):
        p = self._jobs[job_id]
        stderr = bytes(p.readAllStandardError()).decode("utf8")
        stdout = bytes(p.readAllStandardOutput()).decode("utf8")
        output = stderr + stdout

        parser = self._parsers.get(job_id)

        if parser.progress:
            progress = parser.progress(output)
            if progress:
                self._state[job_id]["progress"] = progress
                self.layoutChanged.emit()

        if parser.data:
            data = parser.data(output)
            if data:
                self.result.emit(job_id, data)

    def handle_state(self, job_id, state):
        self._state[job_id]["status"] = state
        self.layoutChanged.emit()

    def done(self, job_id, exit_code, exit_status):
        """
        Task/worker complete. Remove it from the active workers
        dictionary. We leave it in worker_state, as this is used to
        to display past/complete workers too.
        """
        del self._jobs[job_id]
        self.layoutChanged.emit()

    def cleanup(self):
        """
        Remove any complete/failed workers from worker_state.
        """
        for job_id, s in list(self._state.items()):
            if s["status"] == QProcess.NotRunning:
                del self._state[job_id]
        self.layoutChanged.emit()

    # Model interface
    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            job_ids = list(self._state.keys())
            job_id = job_ids[index.row()]
            return job_id, self._state[job_id]

    def rowCount(self, index):
        return len(self._state)


# end::jobManager[]


# tag::delegate[]
class ProgressBarDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # data is our status dict, containing progress, id, status
        job_id, data = index.model().data(index, Qt.DisplayRole)
        if data["progress"] > 0:
            color = QColor(STATUS_COLORS[data["status"]])

            brush = QBrush()
            brush.setColor(color)
            brush.setStyle(Qt.SolidPattern)

            width = option.rect.width() * data["progress"] / 100

            rect = QRect(option.rect)  #  Copy of the rect, so we can modify.
            rect.setWidth(width)

            painter.fillRect(rect, brush)

        pen = QPen()
        pen.setColor(Qt.black)
        painter.drawText(option.rect, Qt.AlignLeft, job_id)


# end::delegate[]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.job = JobManager()

        self.job.status.connect(self.statusBar().showMessage)
        self.job.result.connect(self.display_result)

        layout = QVBoxLayout()

        self.progress = QListView()
        self.progress.setModel(self.job)
        delegate = ProgressBarDelegate()
        self.progress.setItemDelegate(delegate)

        layout.addWidget(self.progress)

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        button = QPushButton("Run a command")
        button.pressed.connect(self.run_command)

        clear = QPushButton("Clear")
        clear.pressed.connect(self.job.cleanup)

        layout.addWidget(self.text)
        layout.addWidget(button)
        layout.addWidget(clear)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

    # tag::startJob[]
    def run_command(self):
        self.job.execute(
            "python",
            ['dummy_script.py'],
            parsers=parsers(progress=simple_percent_parser, data=extract_vars),
        )

    # end::startJob[]

    def display_result(self, job_id, data):
        self.text.appendPlainText("WORKER %s: %s" % (job_id, data))


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
