from app_modules.productListModule.classes.product import Product
from dataclasses import dataclass, field


@dataclass
class ReceiptProduct(Product):
    quantity: int = 1
    total: float = field(init=False)

    def __post_init__(self):
        self.total = self.price * self.quantity
