from typing import List, Optional

from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.products)


if __name__ == "__main__":
    product_1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни.",
        products=[product_1, product_2, product_3],
    )
    print(category.name)
    print(category.description)
    for product in category.products:
        print(f" {product.name}: {product.price} руб.")
    print(f"Количество категорий: {category.category_count}")
    print(f"Количество продуктов в категории: {category.product_count}")
