from PyQt5.QtCore import QStringListModel, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QListWidget, QErrorMessage, QMessageBox, \
    QCompleter

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
        self.init_manage_ui()
        self.init_sell_ui()
        self.search_completer = QCompleter()
        self.search_completer_model = QStringListModel()
        self.search_completer.setModel(self.search_completer_model)
        self.search_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.productsSearch.setCompleter(self.search_completer)
        self.redraw_items()

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

    def redraw_items(self, filtering: str = ""):
        self.ui.productManageList.clear()
        self.ui.allProductsList.clear()
        self.ui.favoriteProductsList.clear()
        self.init_product_system()
        all_products = self.product_system.products
        self.search_completer_model.setStringList([product.name for product in all_products])
        self._draw_items(self.ui.allProductsList, all_products)
        self._draw_items(self.ui.productManageList, all_products)
        self._draw_items(self.ui.favoriteProductsList, self.product_system.favorite_products)

    def init_product_system(self):
        self.product_system.reload_all()

    def init_manage_ui(self):
        def get_current_selected_item() -> QListWidgetItem:
            nonlocal self
            items = self.ui.productManageList.selectedItems()
            if len(items) != 0:
                return items[0]  # ???? ?????????? ???????? ???????????? ????????????,
                # ??.??. selectionMode == Qt::SingleSelection
                # ?? ????, ?????????????? ????, ?????????? ?????????????????????? ?????? ???? ???? ????, ?????? ???????????? ???? ??????????????.
                # ???? ???????????

        def productmanage_edit_dialog(item):
            nonlocal self
            if item:
                widget = self.ui.productManageList.itemWidget(item)
            else:
                widget = None
            self.edit_form = EditForm(widget, self.product_system)
            self.edit_form.setStyleSheet(self.app.styleSheet())
            self.edit_form.show()

        def productmanage_open():
            nonlocal self
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.productManagePage)

        def productmanage_close():
            nonlocal self
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.sellPage)

        def productmanage_edit():
            nonlocal productmanage_edit_dialog
            productmanage_edit_dialog(get_current_selected_item())

        def productmanage_new():
            nonlocal productmanage_edit_dialog
            productmanage_edit_dialog(None)

        def productmanage_remove():
            nonlocal self
            dialog = QMessageBox(self.ui.mainWidget)
            dialog.setText("???? ?????????????????????????? ???????????? ?????????????? ???????????? ???????????")
            dialog.setInformativeText("???????????? ???????????????? ???????????????????? ????????????????.")
            dialog.setIcon(QMessageBox.Warning)
            dialog.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            dialog.setDefaultButton(QMessageBox.No)
            res = dialog.exec()
            if res == QMessageBox.Yes:
                widget = self.ui.productManageList.itemWidget(get_current_selected_item())
                self.product_system.remove_by_name(widget.productName.text())

        # ?????????????????? ?????????????? ?? ??????????????????
        connects = ((self.ui.productManageList.itemDoubleClicked, productmanage_edit_dialog),
                    (self.ui.productManage.triggered, productmanage_open),
                    (self.ui.productManageBack.clicked, productmanage_close),
                    (self.ui.productManageEditProduct.clicked, productmanage_edit),
                    (self.ui.productManageAddProduct.clicked, productmanage_new),
                    (self.ui.productManageRemoveProduct.clicked, productmanage_remove),)

        for action, function in connects:
            action.connect(function)

    def init_sell_ui(self):
        def on_text_change(new_text: str):
            if len(new_text) > 3:
                self.ui.allProductsList.clear()
                self.ui.favoriteProductsList.clear()
                self.product_system.fetch_filtered(new_text)
                self._draw_items(self.ui.allProductsList, self.product_system.products)
                self._draw_items(self.ui.favoriteProductsList, self.product_system.products)
            else:
                self.ui.allProductsList.clear()
                self.ui.favoriteProductsList.clear()
                self.product_system.fetch_all()
                self._draw_items(self.ui.allProductsList, self.product_system.products)
                self._draw_items(self.ui.favoriteProductsList, self.product_system.favorite_products)

        def add_to_receipt(item):
            nonlocal self
            receipt_system = self.app.modules["receiptModule"].receipt_system
            item_widget = self.app.sender().itemWidget(item)
            receipt_system.add_product(
                Product(*self.product_system.get_item_by_name(item_widget.productName.text())))

        # ?????????????????? ?????????????? ?? ??????????????????
        connects = ((self.ui.productsSearch.textChanged, on_text_change),
                    (self.ui.allProductsList.itemDoubleClicked, add_to_receipt),
                    (self.ui.favoriteProductsList.itemDoubleClicked, add_to_receipt))

        for action, function in connects:
            action.connect(function)

    def load(self):
        pass
