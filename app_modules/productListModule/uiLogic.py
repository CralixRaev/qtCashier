from PyQt5.QtWidgets import QListWidgetItem, QWidget

from .classes.product import Product
from ..ABC.uiLogic import ABCUiLogic
from .productSystem import ProductSystem
from .ui.productListItem import Ui_productListItem


class UiLogic(ABCUiLogic):
    def __init__(self, app):
        super().__init__(app)
        self.product_system = ProductSystem(self.config)

        self.init_product_system()
        self.init_ui()

    def _generate_list_item(self):
        widget = QWidget()
        widget_ui = Ui_productListItem()
        widget_ui.setupUi(widget)
        widget_ui.productName.setText('test')
        widget_ui.productPrice.setText(str(200.10))
        return widget

    def init_product_system(self):
        self.product_system.load()
        print(self.product_system.products)

    def init_ui(self):
        item = QListWidgetItem()
        widget = self._generate_list_item()
        item.setSizeHint(widget.size())
        self.ui.allProductsList.addItem(item)
        self.ui.allProductsList.setItemWidget(item, widget)

    def load(self):
        pass