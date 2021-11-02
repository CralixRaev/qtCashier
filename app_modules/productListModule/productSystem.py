import json
from .classes.product import Product
from dacite import from_dict
import sqlite3


class ProductSystem:
    def __init__(self, db_name):
        self.products = []
        self.connection = sqlite3.connect(db_name)

    def load(self):
        pass
