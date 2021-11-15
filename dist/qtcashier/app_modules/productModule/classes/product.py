import io
from dataclasses import dataclass


@dataclass
class Product:
    item_id: int
    name: str = "Новый товар"
    price: float = 0.0
    image: bytes = ""
    is_favorite: bool = False
