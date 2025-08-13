from abc import ABC, abstractmethod
from typing import Any

class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        pass


    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> Any:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs) -> "BaseProduct":
        pass
