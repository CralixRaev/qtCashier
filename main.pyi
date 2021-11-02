from ui.design import Ui_mainWindow


class MainWindow:
    def __init__(self):
        self.opened_classes = {}
        self.modules = {}
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.plugin_system = {}
        self.config = {"product_base_name": None}

    def show(self):
        pass
