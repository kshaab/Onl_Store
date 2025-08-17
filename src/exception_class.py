class ZeroException(Exception):
    def __init__(self, product_name: str) -> None:
        super().__init__(f"В товаре '{product_name}' не указано количество, товар не может быть добавлен.")
