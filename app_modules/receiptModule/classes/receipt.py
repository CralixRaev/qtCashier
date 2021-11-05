from dataclasses import dataclass, field
from typing import Optional

from datetime import datetime

from receiptModule.classes.product import ReceiptProduct


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

    @property
    def total(self):
        return round(sum([product.total for product in self.products]), 2)
