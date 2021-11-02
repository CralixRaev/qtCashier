from PyQt5.QtWidgets import QListWidgetItem, QWidget

from .classes.product import Product
from ..ABC.uiLogic import ABCUiLogic
from .productSystem import ProductSystem
from .ui.productListItem import Ui_productListItem


class UiLogic(ABCUiLogic):
    def __init__(self, app):
        super().__init__(app)
        self.product_system = ProductSystem(self.config["db_name"])
        self.init_product_system()
        self.init_ui()

    def _generate_list_item(self, product: Product):
        widget = QWidget()
        widget_ui = Ui_productListItem()
        widget_ui.setupUi(widget)
        widget_ui.productName.setText(product.name)
        widget_ui.productPrice.setText(str(round(product.price, 2)))
        return widget

    def init_product_system(self):
        self.product_system.load_all()
        print(self.product_system.products)

    def init_ui(self):

        def open_edit_dialog(item):
            nonlocal self
            # edit_form =

        for product in self.product_system.products:
            item = QListWidgetItem()
            widget = self._generate_list_item(product)
            item.setSizeHint(widget.size())
            self.ui.allProductsList.addItem(item)
            self.ui.allProductsList.setItemWidget(item, widget)

        # Соединяем сигналы с функциями
        connects = ((self.ui.productManageList.doubleClicked, open_edit_dialog),)

        for action, function in connects:
            action.connect(function)

    def load(self):
        pass