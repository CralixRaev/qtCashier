import json
from .classes.product import Product
import sqlite3


class ProductSystem:
    def __init__(self, db_name):
        self.products = []
        self.connection = sqlite3.connect(db_name)

    def load_all(self):
        cursor = self.connection.cursor()
        result = cursor.execute("""SELECT id, name, price, picture FROM products""").fetchall()
        for id, name, price, picture in result:
            self.products.append(Product(id, name, price, picture))

    def edit_by_id(self, id: int):
        cursor = self.connection.cursor()
        result = cursor.execute("""""")