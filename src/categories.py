from typing import Any, Iterator, List, Optional

from src.base_order import BaseOrder
from src.product import Product


class CategoryIterator:
    def __init__(self, category_obj: "Category") -> None:
        self.product = category_obj.get_products
        self.index = 0

    def __iter__(self) -> Any:
        return self

    def __next__(self) -> "Product":
        if self.index < len(self.product):
            pr = self.product[self.index]
            self.index += 1
            return pr
        else:
            raise StopIteration


class Category(BaseOrder):
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products_list = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products_list)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products_list)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self) -> Iterator[Product]:
        return CategoryIterator(self)

    def add_product(self, product_name: Any) -> None:
        if not isinstance(product_name, Product):
            print("Объект не принадлежит классу Product")
            return
        self.__products_list.append(product_name)
        Category.product_count += 1

    @property
    def get_products(self) -> List[Product]:
        return self.__products_list

    @property
    def products(self) -> str:
        products_str = ""
        for item in self.__products_list:
            products_str += str(item)
        return products_str

    def count_avg_price(self) -> float:
        try:
            total_price = sum(product.price for product in self.__products_list)
            return round(total_price / len(self.__products_list), 2)
        except ZeroDivisionError:
            return 0




if __name__ == "__main__":
    product_1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни.",
        products=[product_1, product_2, product_3],
    )
    print(f"{category.name}. {category.description}")
    for product in category.get_products:
        print(f" {product.name}: {product.price} руб.")
    print(f"Количество категорий: {category.category_count}")
    print(f"Количество продуктов в категории: {category.product_count}")
    print(category.products)
    print(category)
    for product in category:
        print(product)
    print(category.count_avg_price())
