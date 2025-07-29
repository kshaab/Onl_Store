from unittest.mock import patch, mock_open

from src.utils import read_json, get_products
from src.product import Product
from src.categories import Category





@patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
def test_read_json_success(mock_file):
    result = read_json("dummy.json")
    assert result["key"] == "value"


def test_get_products(sample_data):
    categories = get_products(sample_data.copy())
    assert len(categories) == 2
    assert isinstance(categories[0], Category)
    assert len(categories[0].products) == 2
    assert isinstance(categories[0].products[0], Product)
    assert categories[1].name == "Телевизоры"