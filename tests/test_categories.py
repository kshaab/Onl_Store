from typing import List

import pytest
from _pytest.capture import CaptureFixture

from src.categories import Category, CategoryIterator
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
        "Samsung Galaxy C23 Ultra, 180000.0 руб.Остаток: 5 шт.",
    )
    assert test


def test_add_product(category: Category) -> None:
    count = len(category.get_products)
    new_product = Product("IPhone13", "256GB, Черный", 75000.0, 6)
    category.add_product(new_product)
    assert len(category.get_products) == count + 1
    assert category.get_products[-1] == new_product


def test_add_product_type(capfd: CaptureFixture) -> None:
    category = Category("Смартфоны", "test")
    category.add_product("not available")
    out, _ = capfd.readouterr()
    assert "Объект не принадлежит классу Product" in out
    assert len(category.get_products) == 0


def test_category_str(sample_category: Category) -> None:
    assert "Смартфоны, количество продуктов: 27 шт."


def test_category_iterator(cat_iterator: CategoryIterator) -> None:
    iter(cat_iterator)
    assert cat_iterator.index == 0
    assert next(cat_iterator).name == "Samsung Galaxy C23 Ultra"
    assert next(cat_iterator).name == "Iphone 15"
    assert next(cat_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(cat_iterator)


def test_count_avg_price(category: Category) -> None:
    assert 400333.33


def test_count_avg_price_error(empty_category: Category) -> None:
    assert empty_category.count_avg_price() == 0


def test_add_product_success(capsys: CaptureFixture) -> None:
    category = Category("Смартфоны", "Мобильные устройства", [])

    product = Product("IPhone 14", "256GB, Black", 150000.0, 5)
    category.add_product(product)

    captured = capsys.readouterr()

    assert f"Товар {product.name} успешно добавлен в категорию" in captured.out
    assert "Добавление товара завершено" in captured.out
    assert product in category.get_products
