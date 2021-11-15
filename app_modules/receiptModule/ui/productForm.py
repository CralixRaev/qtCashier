from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox

from productModule.classes.product import Product
from receiptModule.classes.product import ReceiptProduct
from receiptModule.receiptSystem import ReceiptSystem
from receiptModule.ui.productEdit import Ui_Form


class ProductForm(QWidget):
    def __init__(self, receipt_system: ReceiptSystem, product: ReceiptProduct):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.receipt_system = receipt_system
        self.product = product
        self.setup_data()
        self.init_ui()

    def init_ui(self):
        def on_quantity_change(new):
            self.product.quantity = new
            self.ui.quantityEdit.setText(str(new))
            self.ui.totalEdit.setText(str(self.product.total))

        def delete_product():
            dialog = QMessageBox(self)
            dialog.setText("Вы действительно хотите удалить данный товар из чека?")
            dialog.setInformativeText("Данное действие невозможно отменить.")
            dialog.setIcon(QMessageBox.Warning)
            dialog.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            dialog.setDefaultButton(QMessageBox.No)
            dialog.setWindowTitle('УДАЛЕНИЕ ТОВАРА')
            res = dialog.exec()
            if res == QMessageBox.Yes:
                self.receipt_system.current_receipt.products.remove(self.product)
                self.close()

        connects = ((self.ui.ready.clicked, self.close),
                    (self.ui.quantitySpin.valueChanged, on_quantity_change),
                    (self.ui.removeProduct.clicked, delete_product))

        for action, function in connects:
            action.connect(function)

    def setup_data(self):
        self.ui.productName.setText(self.product.name)
        pixmap = QPixmap()
        pixmap.loadFromData(self.product.image)
        self.ui.productImage.setPixmap(pixmap.scaled(512, 512))
        self.ui.quantitySpin.setValue(self.product.quantity)
        self.ui.quantityEdit.setText(str(self.product.quantity))
        self.ui.priceEdit.setText(str(self.product.price))
        self.ui.totalEdit.setText(str(self.product.total))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.receipt_system.redraw_receipt()