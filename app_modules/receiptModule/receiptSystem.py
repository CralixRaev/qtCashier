import datetime
import sqlite3

from productModule.classes.product import Product
from receiptModule.classes.product import ReceiptProduct
from receiptModule.classes.receipt import Receipt


class ReceiptSystem:
    def __init__(self, db_name: str, redraw_receipt):
        self.current_receipt = Receipt()
        self.redraw_receipt = redraw_receipt
        self.connection = sqlite3.connect(db_name)

    def add_product(self, product: Product):
        list_of_ids = [receipt_product.item_id for receipt_product in self.current_receipt.products]
        if product.item_id in list_of_ids:
            self.current_receipt.products[list_of_ids.index(product.item_id)].quantity += 1
        else:
            self.current_receipt.products.append(
                ReceiptProduct(product.item_id, product.name, product.price, product.image,
                               product.is_favorite, 1))
        self.redraw_receipt()

    def clear(self):
        self.current_receipt = Receipt()
        self.redraw_receipt()

    def save_to_db(self):
        cursor = self.connection.cursor()
        result = cursor.execute(
            "INSERT INTO cheque(is_refunded, datetime, comment) VALUES (FALSE, ?, ?)",
            (datetime.datetime.now(), self.current_receipt.comment))
        print(cursor.lastrowid)
        cursor.executemany(
            "INSERT INTO cheque_products(cheque_id, product_id, quantity) VALUES "
            "(?, (SELECT id FROM products WHERE name=?), ?)",
            [(cursor.lastrowid, product.name, product.quantity) for product in
             self.current_receipt.products])
        self.connection.commit()
        self.clear()

    def set_comment(self, comment: str):
        self.current_receipt.comment = comment
