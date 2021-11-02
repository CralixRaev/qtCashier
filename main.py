import importlib
import os
import sys

from PyQt5 import QtWidgets, QtGui
import resources_rc
from ui.design import Ui_mainWindow
from qt_material import apply_stylesheet


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        #   ---------------------------------------------
        #       ЛОГИКА ЗАГРУЗКА МОДУЛЕЙ
        #   ---------------------------------------------
        self.modules = {}
        self.opened_classes = {}
        # я не думаю что мы будем запускаться откуда то кроме самого main.py, поэтому такое
        # решение подойдёт
        path = os.getcwd()
        for app_module in os.listdir(os.path.join(path, 'app_modules')):
            importlib.invalidate_caches()
            if app_module not in ['__pycache__', 'ABC']:
                module = importlib.import_module(f'app_modules.{app_module}.uiLogic')
                self.modules[app_module] = module.UiLogic(self)
                self.opened_classes = self.opened_classes | self.modules[
                    app_module].get_opened_classes()

        for name, module in self.modules.items():
            module.set_opened_classes(self.opened_classes)
            module.load()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml', invert_secondary=False,
                     extra={'font-family': 'Roboto'})
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
