import pytest

from .models import Shoe


@pytest.mark.unit
def test_unit_price_for_total_stock_price():
    shoe = Shoe(stock=100)
    total_stock_price = 1000
    expected = 10

    result = shoe.unit_price_for(total_stock_price)

    assert expected == result


@pytest.mark.unit
def test_unit_price_for_total_stock_price_for_empty_stock():
    shoe = Shoe(stock=0)
    total_stock_price = 1000
    expected = ValueError

    with pytest.raises(expected):
        shoe.unit_price_for(total_stock_price)


@pytest.mark.unit
def test_unit_price_for_total_stock_price_for_invalid_stock_value():
    shoe = Shoe(stock='10')
    total_stock_price = 1000
    expected = ValueError

    with pytest.raises(expected):
        shoe.unit_price_for(total_stock_price)
