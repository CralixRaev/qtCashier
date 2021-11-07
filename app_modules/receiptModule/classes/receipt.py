from dataclasses import dataclass, field
from typing import Optional

from datetime import datetime
from receiptModule.classes.product import ReceiptProduct
import json


@dataclass
class Receipt:
    """
    Класс чека.
    """
    # опциональные элементы - только потому,
    # что до тех пор, пока мы не выбьем чек, мы не знаем его дату-время и прочее
    is_returned: Optional[bool] = None
    date_time: Optional[datetime] = None
    comment: Optional[str] = None
    products: list[ReceiptProduct] = field(default_factory=list)
    item_id: Optional[int] = None

    @property
    def total(self):
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        # знаю, что можно было сделать красивее, но времени нет...
        return round(sum([product.total for product in self.products]),
                     0 if config['receipt']['rounding'] else 2)
