from src.category_iter import CategoryIterator
import pytest

def test_category_iterator(cat_iterator: CategoryIterator) -> None:
    iter(cat_iterator)
    assert cat_iterator.index == 0
    assert next(cat_iterator).name == "Samsung Galaxy C23 Ultra"
    assert next(cat_iterator).name == "Iphone 15"
    assert next(cat_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(cat_iterator)