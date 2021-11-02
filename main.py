import importlib
import os
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QErrorMessage

import resources_rc
from ui.design import Ui_mainWindow
from qt_material import apply_stylesheet
import json


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        #   ---------------------------------------------
        #       ЛОГИКА ЗАГРУЗКА МОДУЛЕЙ
        #   ---------------------------------------------
        # загрузим для начала конфиг
        with open('config.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        self.modules = {}
        self.opened_elems = {}
        # я не думаю что мы будем запускаться откуда то кроме самого main.py, поэтому такое
        # решение подойдёт
        path = os.getcwd()
        for app_module in os.listdir(os.path.join(path, 'app_modules')):
            importlib.invalidate_caches()
            if app_module not in ['__pycache__', 'ABC']:
                module = importlib.import_module(f'app_modules.{app_module}.uiLogic')
                self.modules[app_module] = module.UiLogic(self)

        for name, module in self.modules.items():
            module.load()

    def except_hook(self, cls, exception, traceback):
        QErrorMessage(self).showMessage(str(exception) + str(traceback))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml', invert_secondary=False,
                     extra={'font-family': 'Roboto'})
    window = MainWindow()
    window.show()
    sys.excepthook = window.except_hook
    sys.exit(app.exec())
