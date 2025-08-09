from typing import Any, List

all_products: List["Product"] = []


class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        if type(self) is type(other):
         return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if price < self.price:
            confirm = input("Подтвердите понижение цены. Введите y(yes) или n(no): ").strip().lower()
            if confirm != "y":
                print("Отмена изменения цены")
                return
        self.__price = price

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        for pr in all_products:
            if pr.name.lower() == data["name"].lower():
                pr.quantity += data["quantity"]
                pr.price = data["price"]
                return pr
        new_product = cls(data["name"], data["description"], data["price"], data["quantity"])
        all_products.append(new_product)
        return new_product


if __name__ == "__main__":
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    print(f"{product.name}: {product.description}, {product.price} руб., {product.quantity} шт.")
    another_product = Product("iPhone 14", "256GB, Gray space", 211000.0, 12)
    print(
        f"{another_product.name}: {another_product.description}, {another_product.price}, {another_product.quantity}."
    )
    all_products = []
    Product.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    Product.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB,Белый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    Product.new_product({"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8})
    for product in all_products:
        print(f"{product.name}: {product.description}, {product.price} руб., {product.quantity} шт.")
    print(product.price)
    product.price = -100
    product.price = 200000.0
    print(product.price)
    print(product)
    print(product + another_product)
