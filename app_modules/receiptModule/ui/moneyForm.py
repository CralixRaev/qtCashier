import io
import os

from PyQt5 import QtGui
from PyQt5.QtGui import QPicture, QPixmap
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QFileDialog
from PIL import Image


class EditForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWidget()
        self.ui.setupUi(self)
        self.setup_data()
        self.init_ui()

    def reload_image(self):
        pass

    def setup_data(self):
        pass

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        pass
