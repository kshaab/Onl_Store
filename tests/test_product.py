from typing import Any
from unittest.mock import patch

import pytest

from src.product import Product, all_products


def test_product(product: Product) -> None:
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_property(product: Product) -> None:
    assert product.price == 180000.0


def test_price_fail(capsys: Any) -> None:
    product = Product("Test", "test", 1000, 1)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 1000
    p = Product("Test", "test", 1000, 1)
    p.price = -500
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 1000


@patch("builtins.input", return_value="y")
def test_price_yes(mock_input: Any) -> None:
    product = Product("Test", "test", 1000, 1)
    product.price = 900
    assert product.price == 900


@patch("builtins.input", return_value="n")
def test_price_no(mock_input: Any, capsys: Any) -> None:
    product = Product("Test", "test", 1000, 1)
    product.price = 900
    captured = capsys.readouterr()
    assert "Отмена изменения цены" in captured.out
    assert product.price == 1000


def test_new_product() -> None:
    all_products.clear()
    Product.new_product({"name": "iPhone 14", "description": "test", "price": 200000.0, "quantity": 5})
    new_product = Product.new_product({"name": "iPhone 14", "description": "test", "price": 210000.0, "quantity": 3})
    assert len(all_products) == 1
    assert new_product.quantity == 8
    assert new_product.price == 210000.0


def test_product_str(product: Product) -> None:
    assert str(product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product: Product, other_product: Product) -> None:
    assert product.price + other_product.price == 211000.0
    assert (product.price * product.quantity) + (other_product.price * other_product.quantity) == 1334000.0


def test_product_add_fail(product: Product) -> None:
    with pytest.raises(TypeError):
        product + 1
