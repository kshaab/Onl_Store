from src.product import Product

class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency, model, memory, color) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color




class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, country, germination_period, color) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color




if __name__ == '__main__':
    smartphone = Smartphone("Xiaomi", "1024GB, Синий", 31000.0, 14, 5410, "Redmi Note 11", 128, "Blue")
    print(smartphone.name)
    print(smartphone.description)
    print(smartphone.price)
    print(smartphone.quantity)
    print(smartphone.efficiency)
    print(smartphone.model)
    print(smartphone.memory)
    print(smartphone.color)

    grass = LawnGrass("Grass", "Трава зеленая", 13000, 3, "Germany", "spring", "Green")
    print(grass.name)
    print(grass.description)
    print(grass.price)
    print(grass.quantity)
    print(grass.country)
    print(grass.germination_period)
    print(grass.color)

    # print(smartphone + grass)