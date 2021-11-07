from PyQt5 import QtWidgets
from qt_material import QtStyleTools

from ui.design import Ui_mainWindow


class MainWindow(QtWidgets.QMainWindow, QtStyleTools):
    def __init__(self):
        self.opened_elems = {}
        self.modules = {}
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.plugin_system = {}
        self.config = {"product_base_name": None}

    def show(self):
        pass
