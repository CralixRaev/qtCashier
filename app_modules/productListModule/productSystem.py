import json
from .classes.product import Product
from dacite import from_dict

class ProductSystem:
    def __init__(self):
        self.products = []

    def load(self):
        with open('products.json', 'r') as f:
            for product in json.load(f):
                self.products.append(from_dict(data_class=Product, data=product))
