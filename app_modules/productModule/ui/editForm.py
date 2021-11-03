import os

from PyQt5 import QtGui
from PyQt5.QtGui import QPicture, QPixmap
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QFileDialog
from ..productSystem import ProductSystem
from .productEdit import Ui_mainWidget
from binascii import hexlify


# конечно, это было намного удобнее сделать диалогом, но лицей так не хочет, поэтому отдельная
# формочка, ок


class EditForm(QWidget):
    def __init__(self, clicked_item, product_system, reload_items):
        super().__init__()
        self.ui = Ui_mainWidget()
        self.ui.setupUi(self)
        self.product_system: ProductSystem = product_system
        self.item: tuple = ()
        self.blob_picture: bytes = bytes()
        self.setWindowTitle(f"Редактирование товара | {clicked_item.productName.text()}")
        self.setup_data(clicked_item)
        self.init_ui()
        self.reload_items = reload_items

    def convert_image(self, path: str):
        with open(path, 'rb') as f:
            self.blob_picture = f.read()

    def init_ui(self):
        def ready_button():
            nonlocal self
            self.close()

        def on_barcode_select(item: QListWidgetItem):
            nonlocal self
            self.ui.barcodeEdit.setText(item.text())

        def on_barcode_edit(barcode: str):
            # будто реактивные данные реализовал)
            nonlocal self
            self.ui.barcodeList.selectedItems()[0].setText(barcode)

        def on_file_upload():
            file_path = QFileDialog(self).getOpenFileName(self, 'Выберите изображение товара',
                                                          filter="Изображения (*.png *.jpg *.bmp)")[
                0]  # <-- вот так мне пайчарм круто перенёс строчку)
            self.convert_image(file_path)
            self.reload_image()

        # Соединяем сигналы с функциями
        connects = ((self.ui.readyButton.clicked, ready_button),
                    (self.ui.barcodeList.itemClicked, on_barcode_select),
                    (self.ui.barcodeEdit.textEdited, on_barcode_edit),
                    (self.ui.formUploadImage.clicked, on_file_upload))

        for action, function in connects:
            action.connect(function)

    def reload_image(self):
        pixmap = QPixmap()
        pixmap.loadFromData(self.blob_picture)
        self.ui.imageLabel.setPixmap(pixmap.scaled(256, 256))

    def setup_data(self, starting_item):
        if starting_item:
            self.item = self.product_system.get_item_by_name(starting_item.productName.text())
        else:
            self.item = None
        item_id, name, price, picture, is_favorite = self.item
        self.ui.formNameEdit.setText(name)
        self.ui.formPriceEdit.setValue(price)
        self.ui.formIsFavoriteCheckbox.setChecked(is_favorite or False)
        self.blob_picture = picture
        self.reload_image()
        self.ui.barcodeList.addItems(self.product_system.get_barcodes_by_product_id(item_id))

    def _get_new_values(self) -> tuple:
        name = self.ui.formNameEdit.text()
        price = self.ui.formPriceEdit.value()
        picture = None
        print(os.getcwd())
        is_favorite = self.ui.formIsFavoriteCheckbox.isChecked()
        return name, price, picture, is_favorite

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if self.item:
            self.product_system.update_by_id(self.item[0], self._get_new_values())
            self.product_system.update_by_id_image(self.item[0], self.blob_picture)
            self.reload_items()
        print('I am about to close')
