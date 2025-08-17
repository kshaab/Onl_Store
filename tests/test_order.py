import unittest

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

    def test_init_invalid_quantity_zero(self) -> None:
        with self.assertRaises(ValueError) as context:
            Order(self.product, 0)
        self.assertEqual(str(context.exception), "Товар закончился")

    def test_product_property(self) -> None:
        order = Order(self.product, 1)
        self.assertIs(order.product, self.product)

    def test_str(self) -> None:
        order = Order(self.product, 2)
        expected = "Заказ: Iphone 15, 2 шт., стоимость заказа: 420000.0 руб."
        self.assertEqual(str(order), expected)
