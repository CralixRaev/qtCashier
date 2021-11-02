from PyQt5.QtWidgets import QListWidgetItem, QWidget

from ..ABC.uiLogic import ABCUiLogic
from .ui.checkItem import Ui_receiptItem


class UiLogic(ABCUiLogic):
    def __init__(self, app):
        super().__init__(app)

    def _generate_receipt_item(self, product):
        pass

    def init_ui(self):
        for i in range(3):
            item = QListWidgetItem()
            widget = QWidget()
            widget_ui = Ui_receiptItem()
            widget_ui.setupUi(widget)
            item.setSizeHint(widget.sizeHint())
            self.ui.receiptMainWidget.addItem(item)
            self.ui.receiptMainWidget.setItemWidget(item, widget)

    def load(self):
        self.init_ui()
