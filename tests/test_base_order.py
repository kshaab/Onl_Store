from src.base_order import BaseOrder
import unittest

class TempOrder(BaseOrder):
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"Заказ: {self.name}"

class TestBaseOrder(unittest.TestCase):
    def test_init_and_str(self):
        order = TempOrder("Тест")
        self.assertEqual(order.name, "Тест")
        self.assertEqual(str(order), "Заказ: Тест")
