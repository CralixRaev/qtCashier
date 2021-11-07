import io
import os

from PyQt5 import QtGui
from PyQt5.QtGui import QPicture, QPixmap
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QFileDialog
from PIL import Image

from receiptModule.receiptSystem import ReceiptSystem
from receiptModule.ui.moneyEdit import Ui_Form


class EditForm(QWidget):
    def __init__(self, receipt_system: ReceiptSystem):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.receipt_system = receipt_system
        self.setup_data()
        self.init_ui()
        self.setWindowTitle(f"Итого: {receipt_system.current_receipt.total}")

    def init_ui(self):
        def on_received_change(text):
            nonlocal self
            try:
                change = int(text) - self.receipt_system.current_receipt.total
                if change >= 0:
                    self.ui.changeEdit.setText(f"{change} рублей")
                    self.ui.changeEdit.setStyleSheet("""""")
                    self.ui.totalButton.setDisabled(False)
                else:
                    self.ui.changeEdit.setText(f"Не достаточно денег получено")
                    self.ui.changeEdit.setStyleSheet("""QLabel {
                        color: #ff1b1b
                    }""")
                    self.ui.totalButton.setDisabled(True)
            except ValueError:
                pass

        def total():
            self.receipt_system.save_to_db()
            self.close()

        connects = ((self.ui.receiveEdit.textChanged, on_received_change),
                    (self.ui.totalButton.clicked, total))

        for action, function in connects:
            action.connect(function)

    def setup_data(self):
        receipt = self.receipt_system.current_receipt
        self.ui.receiveEdit.setPlaceholderText(str(receipt.total))
        self.ui.commentEdit.setPlainText(receipt.comment)
