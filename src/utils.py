import json
import os
from typing import Any, Dict, List, cast

from src.categories import Category
from src.product import Product


def read_json(path: str) -> List[Dict[str, Any]]:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        file_data = file_data = cast(List[Dict[str, Any]], json.load(file))
    return file_data


def get_products(file_data: List[Dict[str, Any]]) -> List[Category]:
    categories_list = []
    for cat in file_data:
        products_list = []
        for prod_data in cat["products"]:
            products = Product(
                name=prod_data["name"],
                description=prod_data["description"],
                price=prod_data["price"],
                quantity=prod_data["quantity"],
            )
            products_list.append(products)

        categories = Category(name=cat["name"], description=cat["description"], products=products_list)
        categories_list.append(categories)

    return categories_list


if __name__ == "__main__":
    data = read_json("../data/products.json")
    categories_data = get_products(data)

    for category in categories_data:
        print(f"Категория: {category.name}")
        for product in category.products:
            print(f" {product.name}: {product.price} руб., {product.quantity} шт.")

    print(f"\nВсего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
