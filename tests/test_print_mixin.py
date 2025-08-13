from src.product import Product

def test_print_mixin(capsys):
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    output = capsys.readouterr()
    assert output.out.strip() == "Product(Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
