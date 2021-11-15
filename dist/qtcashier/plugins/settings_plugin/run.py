from PyQt5.QtCore import Qt, QEventLoop
from PyQt5.QtWidgets import QAction, QWidget
from .ui.settingsForm import Ui_Form


class SettingsForm(QWidget):
    def __init__(self, config):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.config = config
        self.init_ui()

    def init_ui(self):
        self.ui.dbNameEdit.setText(self.config['db_name'])
        self.ui.receiptRoundingCheck.setChecked(self.config['receipt']['rounding'])

        def update_db_name(text):
            self.config['db_name'] = text

        def update_receipt_rounding(state):
            self.config['receipt']['rounding'] = state

        def on_close():
            self.close()

        self.ui.dbNameEdit.textChanged.connect(update_db_name)
        self.ui.receiptRoundingCheck.toggled.connect(update_receipt_rounding)
        self.ui.close.clicked.connect(on_close)


def on_reload(application):
    run(application)


def run(application):
    ui = application.ui
    ui.allSettingsAction = QAction("Все настройки")
    ui.settingsMenu.insertAction(ui.settingsPlugins, ui.allSettingsAction)

    def open_form():
        settings_form = SettingsForm(application.config)
        settings_form.setAttribute(Qt.WA_DeleteOnClose)
        settings_form.show()
        settings_form.setStyleSheet(application.styleSheet())
        loop = QEventLoop()
        settings_form.destroyed.connect(loop.quit)
        loop.exec()

    ui.allSettingsAction.triggered.connect(open_form)
