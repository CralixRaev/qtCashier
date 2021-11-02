from ui.design import Ui_mainWindow


class MainWindow:
    def __init__(self):
        self.opened_classes = {}
        self.modules = {}
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.plugin_system = {}

    def show(self):
        pass
