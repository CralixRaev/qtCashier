import datetime

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QListWidget, QInputDialog, QMessageBox

from .classes.product import ReceiptProduct
from .classes.receipt import Receipt
from .receiptSystem import ReceiptSystem
from .ui.productForm import ProductForm
from .ui.receiptItem import Ui_Form
from app_modules.ABC.uiLogic import ABCUiLogic
from .ui.checkItem import Ui_receiptItem
from .ui.moneyForm import EditForm


class ReceiptItem(QWidget, Ui_receiptItem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class AllReceiptsItem(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Signals(QObject):
    new_position = pyqtSignal(dict)
    on_receipt = pyqtSignal(dict)
    on_return = pyqtSignal(QWidget)


class UiLogic(ABCUiLogic):
    def __init__(self, app):
        super().__init__(app)
        self.signals = Signals()
        self.receipt_system = ReceiptSystem(self.config["db_name"],
                                            self.redraw_current_receipt_items,
                                            self.redraw_all_receipts_items, self.signals)

    def _generate_receipt_item(self, i: int, product: ReceiptProduct):
        widget = ReceiptItem()
        widget.itemName.setText(product.name)
        widget.iremPricesPrice.setText(str(round(product.price, 2)))  # ценновые цены)))
        widget.itemPricesQuantity.setText(str(product.quantity))
        widget.itemTotal.setText(f'{product.total}')
        widget.itemId.setText(f'{i}.')
        pixmap = QPixmap()
        pixmap.loadFromData(product.image)
        widget.itemImage.setPixmap(pixmap.scaled(256, 256))
        return widget

    def _generate_all_receipts_item(self, receipt: Receipt):
        widget = AllReceiptsItem()
        widget.timeEdit.setText(receipt.date_time.strftime("%d.%m.%Y %H:%M"))
        widget.idEdit.setText(str(receipt.item_id))
        if receipt.comment:
            widget.commentEdit.setPlainText(receipt.comment)
        else:
            widget.commentEdit.setPlaceholderText("Нет комментария.")
        if receipt.is_returned:
            widget.setDisabled(True)
            widget.idEdit.setText(f'{widget.idEdit.text()} (ВОЗВРАТ)')
        widget.productsWidget.addItems(
            [f"{i}. {product.name} ({product.price} * {product.quantity} = {product.total})" for
             i, product in enumerate(receipt.products, start=1)])
        return widget

    def _draw_items(self, list_widget: QListWidget, products: list[ReceiptProduct]):
        for i, product in enumerate(products, start=1):
            item = QListWidgetItem()
            widget = self._generate_receipt_item(i, product)
            item.setSizeHint(widget.size())
            list_widget.addItem(item)
            list_widget.setItemWidget(item, widget)

    def _draw_receipts(self, list_widget: QListWidget, receipts: list[ReceiptProduct]):
        for receipt in receipts:
            item = QListWidgetItem()
            widget = self._generate_all_receipts_item(receipt)
            item.setSizeHint(widget.size())
            list_widget.addItem(item)
            list_widget.setItemWidget(item, widget)

    def redraw_current_receipt_items(self):
        print('STARTING REDRAW')
        self.ui.receiptMainWidget.clear()
        current_receipt = self.receipt_system.current_receipt
        self._draw_items(self.ui.receiptMainWidget, current_receipt.products)
        self.ui.receiptTotalLabel.setText(f"Итого: {current_receipt.total}")

    def redraw_all_receipts_items(self):
        print('STARTING REDRAW')
        self.receipt_system.fetch_all()
        self.ui.receiptList.clear()
        self._draw_receipts(self.ui.receiptList, self.receipt_system.receipts)

    def redraw_all_receipts_items_by_date(self, from_date: datetime.datetime,
                                          to_date: datetime.datetime):
        print('STARTING REDRAW')
        self.receipt_system.fetch_by_date(from_date, to_date)
        self.ui.receiptList.clear()
        self._draw_receipts(self.ui.receiptList, self.receipt_system.receipts)

    def init_ui(self):
        self.init_sell_page()
        self.init_manage_page()

    def init_manage_page(self):
        def change_page_to_manage():
            nonlocal self
            self.redraw_all_receipts_items()
            from_date, to_date = self.receipt_system.find_from_to_dates_receipts()
            self.ui.receiptListFormFrom.setDateTime(from_date)
            self.ui.receiptListFormTo.setDateTime(to_date)
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.receiptListPage)

        def return_back():
            nonlocal self
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.sellPage)

        def search():
            nonlocal self
            self.redraw_all_receipts_items_by_date(
                self.ui.receiptListFormFrom.dateTime().toPyDateTime(),
                self.ui.receiptListFormTo.dateTime().toPyDateTime())

        def return_receipt(item: QListWidgetItem):
            nonlocal self
            widget = self.ui.receiptList.itemWidget(item)
            if widget.isEnabled():
                dialog = QMessageBox(self.ui.mainWidget, )
                dialog.setText("Вы действительно хотите вернуть данный чек?")
                dialog.setInformativeText("Данное действие невозможно отменить.")
                dialog.setIcon(QMessageBox.Warning)
                dialog.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                dialog.setDefaultButton(QMessageBox.No)
                res = dialog.exec()
                if res == QMessageBox.Yes:
                    self.receipt_system.return_by_id(widget.idEdit.text())
                    widget.setDisabled(True)
                    widget.idEdit.setText(f'{widget.idEdit.text()} (ВОЗВРАТ)')
                    self.signals.on_return.emit(widget)

        # Соединяем сигналы с функциями
        connects = ((self.ui.receiptHistory.triggered, change_page_to_manage),
                    (self.ui.receiptListBackButton.clicked, return_back),
                    (self.ui.receiptListSearch.clicked, search),
                    (self.ui.receiptList.itemDoubleClicked, return_receipt))

        for action, function in connects:
            action.connect(function)

    def init_sell_page(self):
        # Соединяем сигналы с функциями
        def clear_receipt():
            nonlocal self
            if self.receipt_system.current_receipt.products:
                dialog = QMessageBox(self.ui.mainWidget, )
                dialog.setText("Вы действительно хотите очистить данный чек?")
                dialog.setInformativeText("Данное действие невозможно отменить.")
                dialog.setIcon(QMessageBox.Warning)
                dialog.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                dialog.setDefaultButton(QMessageBox.No)
                res = dialog.exec()
                if res == QMessageBox.Yes:
                    self.receipt_system.clear()

        def set_comment(comment: str):
            nonlocal self
            new_comment, is_saved = QInputDialog.getMultiLineText(self.ui.mainWidget,
                                                                  "Введите комментарий к чеку",
                                                                  "Комментарий:",
                                                                  self.receipt_system.current_receipt.comment)
            if is_saved:
                self.receipt_system.set_comment(new_comment)

        def save_receipt():
            nonlocal self
            if self.receipt_system.current_receipt.products:
                self.money_form = EditForm(self.receipt_system, self.signals)
                self.money_form.setStyleSheet(self.app.styleSheet())
                self.money_form.show()

        def edit_product(item):
            nonlocal self
            product = self.receipt_system.current_receipt.products[
                self.ui.receiptMainWidget.indexFromItem(item).row()]
            self.product_form = ProductForm(self.receipt_system, product)
            self.product_form.setStyleSheet(self.app.styleSheet())
            self.product_form.show()

        connects = ((self.ui.receiptHeaderDelete.clicked, clear_receipt),
                    (self.ui.receiptHeaderDescription.clicked, set_comment),
                    (self.ui.receiptTotal.clicked, save_receipt,),
                    (self.ui.receiptMainWidget.itemDoubleClicked, edit_product))

        for action, function in connects:
            action.connect(function)

    def load(self):
        self.init_ui()
