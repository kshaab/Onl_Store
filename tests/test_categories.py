from typing import List

from src.categories import Category
from src.product import Product


def test_category(category: Category) -> None:
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни."
    )
    assert len(category.products) == 3


def test_counts(sample_products: List[Product]) -> None:
    Category.category_count = 0
    Category.product_count = 0
    Category("Смартфоны", "Описание 1", products=sample_products)
    Category("Телевизоры", "Описание 2", products=[Product("LG OLED", "55 дюймов", 100000.0, 3)])
    assert Category.category_count == 2
    assert Category.product_count == 4
