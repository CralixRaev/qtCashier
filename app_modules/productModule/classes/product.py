import io
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float
    image: bytes
