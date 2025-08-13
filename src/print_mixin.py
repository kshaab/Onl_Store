from typing import Any


class PrintMixin:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
