from typing import Optional

from app_modules.productModule.classes.product import Product
from dataclasses import dataclass, field


@dataclass
class ReceiptProduct(Product):
    item_id: Optional[int] = None
    quantity: int = 1

    @property
    def total(self):
        return round(self.price * self.quantity, 2)
