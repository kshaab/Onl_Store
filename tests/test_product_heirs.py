import pytest

from src.product_heirs import LawnGrass, Smartphone


def test_smartphone_init(smartphone: Smartphone) -> None:
    assert smartphone.name == "IPhone16e"
    assert smartphone.description == "256GB, Белый"
    assert smartphone.price == 90000.0
    assert smartphone.quantity == 14
    assert smartphone.efficiency == 5410
    assert smartphone.model == "A3212"
    assert smartphone.memory == 256
    assert smartphone.color == "White"


def test_grass_init(grass: LawnGrass) -> None:
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_add_fail(smartphone: Smartphone, grass: LawnGrass) -> None:
    with pytest.raises(TypeError):
        smartphone + grass
