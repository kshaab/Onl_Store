import pytest

from src.exception_class import ZeroException


def test_zero_exception_message() -> None:
    product_name = "IPhone 15"
    with pytest.raises(ZeroException) as e:
        raise ZeroException(product_name)
    assert e.type == ZeroException
    assert str(e.value) == f"В товаре '{product_name}' не указано количество, товар не может быть добавлен."
