from typing import Any, Dict, List
from unittest.mock import mock_open, patch

from src.categories import Category
from src.product import Product
from src.utils import get_products, read_json


@patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
def test_read_json_success(mock_file: Any) -> None:
    result = read_json("dummy.json")
    assert result["key"] == "value"


def test_get_products(sample_data: List[Dict[str, Any]]) -> None:
    categories = get_products(sample_data.copy())
    assert len(categories) == 2
    assert isinstance(categories[0], Category)
    assert len(categories[0].get_products) == 2
    assert isinstance(categories[0].get_products[0], Product)
    assert categories[1].name == "Телевизоры"
