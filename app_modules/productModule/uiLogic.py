from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QListWidget

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
        self.product_system = ProductSystem(self.config["db_name"], self.redraw_items)
        self.init_ui()

    def _generate_list_item(self, product: Product):

        widget = ListItem()
        widget.productName.setText(product.name)
        widget.productPrice.setText(str(round(product.price, 2)))
        pixmap = QPixmap()
        pixmap.loadFromData(product.image)
        widget.productImage.setPixmap(pixmap.scaled(256, 256))

        def update_favorite():
            nonlocal widget, self
            name, is_favorite = widget.productName.text(), widget.favoriteCheckBox.isChecked()
            self.product_system.update_by_name_favorite(name, is_favorite)

        widget.favoriteCheckBox.setChecked(product.is_favorite)
        widget.favoriteCheckBox.clicked.connect(update_favorite)
        return widget

    def _draw_items(self, list_widget: QListWidget, products: list):
        for product in products:
            item = QListWidgetItem()
            widget = self._generate_list_item(product)
            item.setSizeHint(widget.size())
            list_widget.addItem(item)
            list_widget.setItemWidget(item, widget)

    def redraw_items(self):
        print('STARTING REDRAW')
        self.ui.productManageList.clear()
        self.ui.allProductsList.clear()
        self.ui.favoriteProductsList.clear()
        self.init_product_system()
        all_products = self.product_system.products
        self._draw_items(self.ui.allProductsList, all_products)
        self._draw_items(self.ui.productManageList, all_products)
        self._draw_items(self.ui.favoriteProductsList, self.product_system.favorite_products)

    def init_product_system(self):
        self.product_system.reload_all()

    def init_ui(self):

        def open_edit_dialog(item):
            nonlocal self
            widget = self.ui.productManageList.itemWidget(item)
            self.edit_form = EditForm(widget, self.product_system)
            self.edit_form.show()

        def productmanage_open():
            nonlocal self
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.productManagePage)

        def productmanage_close():
            nonlocal self
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.sellPage)

        self.redraw_items()

        # Соединяем сигналы с функциями
        connects = ((self.ui.productManageList.itemDoubleClicked, open_edit_dialog),
                    (self.ui.productManage.triggered, productmanage_open),
                    (self.ui.productManageBack.clicked, productmanage_close))

        for action, function in connects:
            action.connect(function)

    def load(self):
        pass
