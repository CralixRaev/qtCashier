import io
import os

from PyQt5 import QtGui
from PyQt5.QtGui import QPicture, QPixmap
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QFileDialog
from ..productSystem import ProductSystem
from .productEdit import Ui_mainWidget
from PIL import Image


# конечно, это было намного удобнее сделать диалогом, но лицей так не хочет, поэтому отдельная
# формочка, ок

def crop_center(img: Image.Image, crop_width: int, crop_height: int) -> Image:
    """
    Функция для обрезки изображения по центру.
    """
    img_width, img_height = img.size
    return img.crop(((img_width - crop_width) // 2,
                     (img_height - crop_height) // 2,
                     (img_width + crop_width) // 2,
                     (img_height + crop_height) // 2))


def crop_max_square(img: Image.Image) -> Image:
    return crop_center(img, min(img.size), min(img.size))


class EditForm(QWidget):
    def __init__(self, clicked_item, product_system):
        super().__init__()
        self.ui = Ui_mainWidget()
        self.ui.setupUi(self)
        self.product_system: ProductSystem = product_system
        self.item: tuple = ()
        self.blob_picture: bytes = bytes
        self.convert_image(os.path.join(os.getcwd(), 'no-image.png'))
        self.setWindowTitle(
            f"Редактирование товара | "
            f"{clicked_item.productName.text() if clicked_item else 'Новый товар'}")
        self.setup_data(clicked_item)
        self.init_ui()

    def convert_image(self, path: str):
        im = Image.open(path)
        im = crop_max_square(im)
        stream = io.BytesIO()
        im.save(stream, format="PNG")
        self.blob_picture = stream.getvalue()

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
        self.ui.imageLabel.setPixmap(pixmap.scaled(1024, 1024))

    def setup_data(self, starting_item):
        item_id, name, price, picture, is_favorite = (None,) * 5  # костыль
        if starting_item:
            self.item = self.product_system.get_item_by_name(starting_item.productName.text())
            item_id, name, price, picture, is_favorite = self.item
            self.blob_picture = picture
            self.ui.barcodeList.addItems(self.product_system.get_barcodes_by_product_id(item_id))
        else:
            self.item = None
        self.ui.formNameEdit.setText(name or 'Новый товар')
        self.ui.formPriceEdit.setValue(price or 0.00)
        self.ui.formIsFavoriteCheckbox.setChecked(is_favorite or False)
        self.reload_image()

    def _get_new_values(self) -> tuple:
        name = self.ui.formNameEdit.text()
        price = self.ui.formPriceEdit.value()
        picture = None
        is_favorite = self.ui.formIsFavoriteCheckbox.isChecked()
        return name, price, is_favorite

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if self.item:
            self.product_system.update_by_id(self.item[0], self._get_new_values())
            self.product_system.update_by_id_image(self.item[0], self.blob_picture)
        else:
            self.product_system.create_new(self._get_new_values(), self.blob_picture)
        print('I am about to close')
