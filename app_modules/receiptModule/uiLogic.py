from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QListWidget, QInputDialog, QMessageBox

from productModule.classes.product import Product
from .classes.product import ReceiptProduct
from .receiptSystem import ReceiptSystem
from ..ABC.uiLogic import ABCUiLogic
from .ui.checkItem import Ui_receiptItem
from .ui.moneyForm import MoneyForm

class ReceiptItem(QWidget, Ui_receiptItem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class UiLogic(ABCUiLogic):
    def __init__(self, app):
        super().__init__(app)
        self.receipt_system = ReceiptSystem(self.config["db_name"], self.redraw_current_receipt_items)

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

    def _draw_items(self, list_widget: QListWidget, products: list[ReceiptProduct]):
        for i, product in enumerate(products, start=1):
            item = QListWidgetItem()
            widget = self._generate_receipt_item(i, product)
            item.setSizeHint(widget.size())
            list_widget.addItem(item)
            list_widget.setItemWidget(item, widget)

    def redraw_current_receipt_items(self):
        print('STARTING REDRAW')
        self.ui.receiptMainWidget.clear()
        current_receipt = self.receipt_system.current_receipt
        self._draw_items(self.ui.receiptMainWidget, current_receipt.products)
        self.ui.receiptTotalLabel.setText(f"Итого: {current_receipt.total}")

    def init_ui(self):
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
                                                        "Введите комментарий к чеку", "Комментарий:",
                                                        self.receipt_system.current_receipt.comment)
            if is_saved:
                self.receipt_system.set_comment(new_comment)

        def save_receipt():
            money_form = MoneyForm()
            self.receipt_system.save_to_db()

        connects = ((self.ui.receiptHeaderDelete.clicked, clear_receipt),
                    (self.ui.receiptHeaderDescription.clicked, set_comment),
                    (self.ui.receiptTotal.clicked, save_receipt))

        for action, function in connects:
            action.connect(function)

    def load(self):
        self.init_ui()
