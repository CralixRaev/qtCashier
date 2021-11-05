from dataclasses import dataclass, field
from typing import Optional

import datetime as datetime

from receiptModule.classes.product import ReceiptProduct


@dataclass
class Receipt:
    """
    Класс чека.
    """
    # опциональные элементы - только потому,
    # что до тех пор, пока мы не выбьем чек, мы не знаем его дату-время и прочее
    is_returned: Optional[bool]
    date_time: Optional[datetime]
    products: list[ReceiptProduct] = field(default_factory=list)
