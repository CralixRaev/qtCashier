import importlib
import os
import sys
import ctypes
import traceback

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import qWarning, qCritical
from PyQt5.QtWidgets import QErrorMessage

import resources_rc
from ui.design import Ui_mainWindow
from qt_material import QtStyleTools
import json


class MainWindow(QtWidgets.QMainWindow, QtStyleTools):
    def __init__(self):
        super().__init__()
        # загрузим для начала конфиг
        with open('config.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        self.ui = Ui_mainWindow()
        self.apply_stylesheet(self, theme=f'{self.config["current_theme"]}_blue.xml',
                              invert_secondary=False if self.config[
                                                            "current_theme"] == 'dark' else True,
                              extra={'font-family': 'Roboto'})
        self.ui.setupUi(self)
        #   ---------------------------------------------
        #       ЛОГИКА ЗАГРУЗКА МОДУЛЕЙ
        #   ---------------------------------------------
        self.modules = {}
        self.opened_elems = {}
        # я не думаю что мы будем запускаться откуда то кроме самого run.py, поэтому такое
        # решение подойдёт
        path = os.getcwd()
        for app_module in os.listdir(os.path.join(path, 'app_modules')):
            importlib.invalidate_caches()
            if app_module not in ['__pycache__', 'ABC']:
                module = importlib.import_module(f'app_modules.{app_module}.uiLogic')
                self.modules[app_module] = module.UiLogic(self)

        for name, module in self.modules.items():
            module.load()

    def except_hook(self, cls, exception, tb):
        nest_dir = os.path.dirname(os.path.abspath(__file__))
        traceback_str = ''
        idx = 0
        for file_name, line_number, func_name, text in traceback.extract_tb(tb)[1:]:
            # skip Nest-related tracebacks to make it more readable
            if os.path.dirname(os.path.abspath(file_name)) == nest_dir:
                continue
            idx += 1
            traceback_str += '\n  [%d] File "%s", line %d, in function "%s"\n    %s' % \
                             (idx, file_name, line_number, func_name, text)
        qCritical(str(exception) + traceback_str)
        QErrorMessage(self).showMessage(str(exception) + traceback_str)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        for name, module in self.modules.items():
            if hasattr(module, 'on_app_close'):
                module.on_app_close()
            else:
                qWarning(f"Module {module.__class__} doesn't have on_app_close method")
                # london is a capital of great britain

        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(self.config, f)


def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print(f'qt_message_handler: line: {context.line}, func: {context.function}, file: {context.file}')
    print(f'  {mode}: {message}\n')


QtCore.qInstallMessageHandler(qt_message_handler)


if __name__ == "__main__":
    # хак, что бы сказать что pythonw.exe является
    # хостом для других приложений (помогает в отрисовке иконки в таскбаре)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'cralix_project.QtCashier.beta.1')
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.excepthook = window.except_hook
    sys.exit(app.exec())
