import unittest

import pytest

from src.order import Order
from src.product import Product


class TestOrder(unittest.TestCase):
    def setUp(self) -> None:
        self.product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    def test_init_valid(self) -> None:
        order = Order(self.product, 2)
        self.assertEqual(order.product, self.product)
        self.assertEqual(order.quantity, 2)
        self.assertEqual(order.total_price, 420000.0)

    def test_product_property(self) -> None:
        order = Order(self.product, 1)
        self.assertIs(order.product, self.product)

    def test_str(self) -> None:
        order = Order(self.product, 2)
        expected = "Заказ: Iphone 15, 2 шт., стоимость заказа: 420000.0 руб."
        self.assertEqual(str(order), expected)


def test_order_with_valid_quantity(capsys: pytest.CaptureFixture[str]) -> None:
    product = Product("IPhone 13", "256GB, Черный", 75000.0, 2)
    Order(product, 2)

    captured = capsys.readouterr()
    assert "успешно добавлен в заказ" in captured.out
    assert "Добавление товара завершено" in captured.out


def test_order_with_zero_quantity_raises_zero_exception(capsys: pytest.CaptureFixture[str]) -> None:
    product = Product("IPhone 14", "128GB, Белый", 85000.0, 5)

    Order(product, 0)

    captured = capsys.readouterr()
    assert "не указано количество" in captured.out
    assert "Добавление товара завершено" in captured.out
