
from src.product import Product
from src.base_order import BaseOrder

class Order(BaseOrder):
    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Товар закончился")
        self._product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    @property
    def product(self) -> Product:
        return self._product

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, {self.quantity} шт., стоимость заказа: {self.total_price} руб."

if __name__ == "__main__":
    p = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    order = Order(p, 2)
    print(order)




    
    




