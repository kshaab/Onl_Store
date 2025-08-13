from src.product import Product

class Order:
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
        return (
            f"Заказ: {self.product.name} — {self.quantity} шт., "
            f"итоговая стоимость: {self.total_price} руб."
        )

if __name__ == "__main__":
    p = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    order = Order(p, 2)
    print(order)




    
    




