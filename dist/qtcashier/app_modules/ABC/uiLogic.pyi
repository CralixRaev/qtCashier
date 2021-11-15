from PyQt5.QtCore import QObject

from main import MainWindow

class ABCUiLogic:
    def __init__(self, app: MainWindow):
        self.app = app
        self.ui = app.ui
        self.config = app.config
        ...

class ABCSignals(QObject):
    pass