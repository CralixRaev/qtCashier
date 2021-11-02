from PyQt5.QtWidgets import QWidget

from .productEdit import Ui_mainWidget


# конечно, это было намного удобнее сделать диалогом, но лицей так не хочет, поэтому отдельная
# формочка, ок

class EditForm(QWidget):
    def __init__(self, clicked_item):
        super().__init__()
        self.ui = Ui_mainWidget()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Редактирование товара | {clicked_item.productName.text()}")