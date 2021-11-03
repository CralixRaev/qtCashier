import io
from dataclasses import dataclass


@dataclass
class Product:
    item_id: int
    name: str
    price: float
    image: bytes
    is_favorite: bool
