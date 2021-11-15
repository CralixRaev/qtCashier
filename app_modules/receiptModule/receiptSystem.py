import datetime
import sqlite3

from ..productModule.classes.product import Product
from .classes.product import ReceiptProduct
from .classes.receipt import Receipt


class ReceiptSystem:
    def __init__(self, db_name: str, redraw_receipt, redraw_all_receipts, signals):
        self.receipts = []
        self.current_receipt = Receipt()
        self.redraw_receipt = redraw_receipt
        self.redraw_all_receipts = redraw_all_receipts
        self.connection = sqlite3.connect(db_name)
        self.signals = signals

    def add_product(self, product: Product):
        list_of_ids = [receipt_product.item_id for receipt_product in self.current_receipt.products]
        if product.item_id in list_of_ids:
            self.current_receipt.products[list_of_ids.index(product.item_id)].quantity += 1
        else:
            self.current_receipt.products.append(
                ReceiptProduct(product.item_id, product.name, product.price, product.image,
                               product.is_favorite, 1))
        self.signals.new_position.emit(product.__dict__)
        self.redraw_receipt()

    def clear(self):
        """
        Функция очистки чека
        Полностью очищает текущий чек и перерисовывает его
        :return:
        """
        self.current_receipt = Receipt()
        self.receipts = []
        self.redraw_receipt()

    def save_to_db(self):
        """
        Сохраняет текущий чек
        :return:
        """
        cursor = self.connection.cursor()
        result = cursor.execute(
            "INSERT INTO cheque(is_refunded, datetime, comment) VALUES (FALSE, ?, ?)",
            (datetime.datetime.now(), self.current_receipt.comment))
        self.current_receipt.item_id = result.lastrowid
        cursor.executemany(
            "INSERT INTO cheque_products(cheque_id, product_id, quantity) VALUES "
            "(?, (SELECT id FROM products WHERE name=?), ?)",
            [(cursor.lastrowid, product.name, product.quantity) for product in
             self.current_receipt.products])
        self.connection.commit()
        self.signals.on_receipt.emit(self.current_receipt.__dict__)
        self.clear()

    def fetch_all(self):
        self.receipts = []
        cursor = self.connection.cursor()
        receipts = cursor.execute("""SELECT * FROM cheque ORDER BY datetime DESC""").fetchall()
        for item_id, is_returned, date_time, comment in receipts:
            result = cursor.execute("""SELECT p.id, p.name, p.price, p.picture, p.is_favorite, c.quantity
            FROM cheque_products c
            LEFT JOIN products p on p.id = c.product_id
            WHERE cheque_id = ?""", (item_id,)).fetchall()
            products = [
                ReceiptProduct(*product) if product[0] else ReceiptProduct(None, "Удалённый товар")
                for product in result]
            self.receipts.append(
                Receipt(is_returned, datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S.%f"),
                        comment, products, item_id))

    def fetch_by_date(self, from_date: datetime.datetime, to_date: datetime.datetime):
        self.receipts = []
        cursor = self.connection.cursor()
        receipts = cursor.execute("""SELECT * 
        FROM cheque 
        WHERE datetime BETWEEN ? AND ? 
        ORDER BY datetime DESC""", (from_date, to_date)).fetchall()
        for item_id, is_returned, date_time, comment in receipts:
            result = cursor.execute("""SELECT p.id, p.name, p.price, p.picture, p.is_favorite, c.quantity
            FROM cheque_products c
            LEFT JOIN products p on p.id = c.product_id
            WHERE cheque_id = ? """, (item_id,)).fetchall()
            products = [
                ReceiptProduct(*product) if product[0] else ReceiptProduct(None, "Удалённый товар")
                for product in result]
            self.receipts.append(
                Receipt(is_returned, datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S.%f"),
                        comment, products, item_id))

    def get_by_id(self):
        pass

    def find_from_to_dates_receipts(self):
        return min(self.receipts, key=lambda x: x.date_time).date_time, \
               max(self.receipts, key=lambda x: x.date_time).date_time

    def return_by_id(self, item_id: str):
        cursor = self.connection.cursor()
        cursor.execute("""UPDATE cheque SET is_refunded=TRUE WHERE id = ?""", (item_id,))
        self.connection.commit()

    def set_comment(self, comment: str):
        self.current_receipt.comment = comment
