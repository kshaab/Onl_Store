from src.base_order import BaseOrder
from src.product import Product
from exception_class import ZeroException


class Order(BaseOrder):
    def __init__(self, product: Product, quantity: int) -> None:
        self._product = product
        self.quantity = quantity
        self.total_price = product.price * quantity
        try:
            if quantity <= 0:
                raise ZeroException(product.name)
            print(f"Товар {product.name} успешно добавлен в заказ")
        except ZeroException as e:
            print(e)
        finally:
            print("Добавление товара завершено")


    @property
    def product(self) -> Product:
        return self._product

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, {self.quantity} шт., стоимость заказа: {self.total_price} руб."


if __name__ == "__main__":
    p = Product("Iphone 15", "512GB, Gray space", 210000.0, 3)
    order = Order(p, 2)
    print(order)
