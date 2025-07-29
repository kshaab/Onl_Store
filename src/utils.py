import json
import os
from src.product import Product
from src.categories import Category

def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as file:
        file_data = json.load(file)
    return file_data


def get_products(file_data):
    categories_list = []
    for cat in file_data:
        products_list = []
        for prod_data in cat['products']:
            products = Product(
                name=prod_data['name'],
                description=prod_data['description'],
                price=prod_data['price'],
                quantity=prod_data['quantity']
            )
            products_list .append(products)

        categories = Category(
            name= cat['name'],
            description= cat['description'],
            products=products_list
        )
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
