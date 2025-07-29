from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_amount = 0
    product_amount = 0
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_amount += 1
        Category.product_amount += len(products)

if __name__ == "__main__":
  product_1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
  product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
  product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

  category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни", products=[product_1, product_2, product_3])
  print(category.name)
  print(category.description)
  print(category.products)
  print(category.product_amount)
  print(category.category_amount)