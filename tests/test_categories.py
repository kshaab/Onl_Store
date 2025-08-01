from typing import List

from src.categories import Category
from src.product import Product


def test_category(category: Category) -> None:
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни."
    )
    assert len(category.get_products) == 3


def test_counts(sample_products: List[Product]) -> None:
    Category.category_count = 0
    Category.product_count = 0
    Category("Смартфоны", "Описание 1", products=sample_products)
    Category("Телевизоры", "Описание 2", products=[Product("LG OLED", "55 дюймов", 100000.0, 3)])
    assert Category.category_count == 2
    assert Category.product_count == 4

def test_get_products_property(category: Category) -> None:
    assert len(category.get_products) == 3
    assert all(isinstance(p, Product) for p in category.get_products)

def test_products(sample_products: List[Product]) -> None:
    test = (
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
        "Iphone 15, 210000.0 руб.Остаток: 8 шт.",
        "Samsung Galaxy C23 Ultra, 180000.0 руб.Остаток: 5 шт."
    )
    assert test

def test_add_product(category: Category) -> None:
    count = len(category.get_products)
    new_product = Product("IPhone13", "256GB, Черный", 75000.0, 6)
    category.add_product(new_product)
    assert len(category.get_products) == count + 1
    assert category.get_products[-1] == new_product




