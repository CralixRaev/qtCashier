from PyQt5.QtWidgets import QListWidgetItem, QWidget

from .classes.product import Product
from .ui.editForm import EditForm
from ..ABC.uiLogic import ABCUiLogic
from .productSystem import ProductSystem
from .ui.productListItem import Ui_productListItem


class ListItem(QWidget, Ui_productListItem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class UiLogic(ABCUiLogic):
    def __init__(self, app):
        super().__init__(app)
        self.product_system = ProductSystem(self.config["db_name"])
        self.init_product_system()
        self.init_ui()

    def _generate_list_item(self, product: Product):
        widget = ListItem()
        widget.productName.setText(product.name)
        widget.productPrice.setText(str(round(product.price, 2)))
        return widget

    def init_product_system(self):
        self.product_system.load_all()
        print(self.product_system.products)

    def init_ui(self):

        def open_edit_dialog(item):
            nonlocal self
            widget = self.ui.productManageList.itemWidget(item)
            self.edit_form = EditForm(widget)
            self.edit_form.show()

        def productmanage_open():
            nonlocal self
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.productManagePage)

        def productmanage_close():
            nonlocal self
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.sellPage)

        for product in self.product_system.products:
            item = QListWidgetItem()
            widget = self._generate_list_item(product)
            item.setSizeHint(widget.size())
            self.ui.allProductsList.addItem(item)
            self.ui.allProductsList.setItemWidget(item, widget)

        for product in self.product_system.products:
            item = QListWidgetItem()
            widget = self._generate_list_item(product)
            item.setSizeHint(widget.size())
            self.ui.productManageList.addItem(item)
            self.ui.productManageList.setItemWidget(item, widget)

        # Соединяем сигналы с функциями
        connects = ((self.ui.productManageList.itemDoubleClicked, open_edit_dialog),
                    (self.ui.productManage.triggered, productmanage_open),
                    (self.ui.productManageBack.clicked, productmanage_close))

        for action, function in connects:
            action.connect(function)

    def load(self):
        pass