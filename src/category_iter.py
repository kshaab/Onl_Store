class CategoryIterator:
    def __init__(self, category) -> None:
        self.product = category.get_products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.product):
            product = self.product[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration




