from .classes.product import Product
import sqlite3


# честно скажу, хотел это сделать больше похожим на какой-то ORM, но время поджимает и просто сложно
class ProductSystem:
    def __init__(self, db_name: str, redraw_items):
        self.products = []
        self.favorite_products = []
        self.redraw_items = redraw_items
        self.connection = sqlite3.connect(db_name)

    def fetch_all(self):
        cursor = self.connection.cursor()
        self.products = []
        result = cursor.execute(
            """SELECT id, name, price, picture, is_favorite FROM products""").fetchall()
        for item_id, name, price, picture, is_favorite in result:
            self.products.append(Product(item_id, name, price, picture, is_favorite))

    def fetch_filtered(self, name: str):
        cursor = self.connection.cursor()
        self.products = []
        result = cursor.execute(
            f"""SELECT id, name, price, picture, is_favorite FROM products 
            WHERE name GLOB ?""", (f'*{name}*',)).fetchall()
        for item_id, name, price, picture, is_favorite in result:
            self.products.append(Product(item_id, name, price, picture, is_favorite))

    def fetch_favorite(self):
        cursor = self.connection.cursor()
        self.favorite_products = []
        result = cursor.execute(
            """SELECT id, name, price, picture, is_favorite 
            FROM products 
            WHERE is_favorite=true""").fetchall()
        for item_id, name, price, picture, is_favorite in result:
            self.favorite_products.append(Product(item_id, name, price, picture, is_favorite))

    def create_new(self, data: tuple, image: bytes):
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO products(name, price, is_favorite, picture)
         VALUES (?, ?, ?, ?)""", (*data, image))
        self.connection.commit()
        self.redraw_items()

    def remove_by_name(self, name: str):
        cursor = self.connection.cursor()
        cursor.execute("""DELETE FROM products WHERE name=?""", (name,))
        self.connection.commit()
        self.redraw_items()

    def reload_all(self):
        self.fetch_all()
        self.fetch_favorite()

    def get_item_by_name(self, name: str) -> tuple:
        cursor = self.connection.cursor()
        return cursor.execute("""SELECT id, name, price, picture, is_favorite
        FROM products 
        WHERE name=?""", (name,)).fetchone()

    def get_barcodes_by_product_id(self, product_id: int) -> list:
        cursor = self.connection.cursor()
        return [barcode[0] for barcode in cursor.execute("""SELECT barcode
                FROM barcode 
                WHERE product_id=?""", (product_id,)).fetchmany()]

    def update_by_id(self, item_id: int, new_data: tuple):
        cursor = self.connection.cursor()
        cursor.execute("""UPDATE products SET name = ?,
        price=?, is_favorite=? WHERE id=?;""", (*new_data, item_id))
        self.connection.commit()
        self.redraw_items()

    def update_by_id_image(self, item_id: int, new_photo: bytes):
        cursor = self.connection.cursor()
        cursor.execute("""UPDATE products SET picture=? WHERE id=?;""", (new_photo, item_id))
        self.connection.commit()
        self.redraw_items()

    def update_by_name_favorite(self, name: str, is_favorite: bool):
        cursor = self.connection.cursor()
        print(f'UPDATING {is_favorite}')
        result = cursor.execute("""UPDATE products SET is_favorite=? WHERE name=?;""",
                                (is_favorite, name))
        self.connection.commit()
        self.redraw_items()

    def update_insert_by_id_barcodes(self, product_id: int, barcodes: list[str]):
        cursor = self.connection.cursor()
        cursor.executemany("""INSERT OR REPLACE INTO barcode(barcode, product_id)
         VALUES (?, ?)""", [(barcode, product_id) for barcode in barcodes])
        self.connection.commit()

    def delete_by_barcode_barcode(self, barcode: str):
        cursor = self.connection.cursor()
        cursor.execute("""DELETE FROM barcode WHERE barcode=?""", (barcode,))
