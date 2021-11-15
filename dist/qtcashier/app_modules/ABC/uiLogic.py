from PyQt5.QtCore import QObject


class ABCUiLogic:
    def __init__(self, app):
        self.app = app
        self.ui = app.ui
        self.config = app.config
