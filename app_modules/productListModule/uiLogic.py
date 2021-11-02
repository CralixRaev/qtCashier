from PyQt5.QtWidgets import QListWidgetItem, QWidget

from .classes.product import Product
from ..ABC.uiLogic import ABCUiLogic
from .productSystem import ProductSystem
from .ui.productListItem import Ui_productListItem


class UiLogic(ABCUiLogic):
    def __init__(self, app):
        super().__init__(app)
        self.product_system = ProductSystem()

        self.init_product_system()
        self.init_ui()

    def _generate_list_item(self, product: Product):
        widget = QWidget()
        widget_ui = Ui_productListItem()
        widget_ui.setupUi(widget)
        widget_ui.productName.setText(product.name)
        widget_ui.productPrice.setText(str(product.price))
        return widget

    def init_product_system(self):
        self.product_system.load()
        print(self.product_system.products)

    def init_ui(self):
        for product in self.product_system.products:
            item = QListWidgetItem()
            widget = self._generate_list_item(product)
            item.setSizeHint(widget.sizeHint())
            self.ui.productsList.addItem(item)
            self.ui.productsList.setItemWidget(item, widget)

    def load(self):
        pass
