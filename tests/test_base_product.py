import unittest
from typing import Any
from unittest.mock import patch

from src.base_product import BaseProduct


class TempProduct(BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        self._price = value

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "TempProduct") -> float:
        return self.price + other.price

    @classmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> "TempProduct":
        return cls(*args, **kwargs)


class TestBaseProduct(unittest.TestCase):
    def test_init(self) -> None:
        product = TempProduct("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        self.assertEqual(
            product.name,
            "Xiaomi Redmi Note 11",
        )
        self.assertEqual(product.description, "1024GB, Синий")
        self.assertEqual(product.price, 31000.0)
        self.assertEqual(product.quantity, 14)

    def test_price(self) -> None:
        product = TempProduct("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        self.assertEqual(product.price, 31000.0)

    def test_price_setter_increase(self) -> None:
        product = TempProduct("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        product.price = 35000.0
        self.assertEqual(product.price, 35000.0)

    @patch("builtins.input", return_value="y")
    def test_price_setter_decrease_y(self, mock_input: Any) -> None:
        product = TempProduct("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        product.price = 30000.0
        self.assertEqual(product.price, 30000.0)

    @patch("builtins.input", return_value="n")
    def test_price_setter_decrease_n(self, mock_input: Any) -> None:
        product = TempProduct("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        product.price = 30000.0
        self.assertEqual(product.price, 30000.0)

    def test_str(self) -> None:
        product = TempProduct("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        expected = "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
        self.assertEqual(str(product), expected)

    def test_add(self) -> None:
        product = TempProduct("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        other_product = TempProduct("iPhone 14", "256GB, Gray space", 211000.0, 12)
        self.assertEqual(product + other_product, 242000)
