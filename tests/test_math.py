import pytest


def test_addition():
    assert 1 + 1 == 2


def test_subtraction():
    assert 1 - 1 == 0


@pytest.mark.parametrize("a, b, product", [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15), (-4, -5, 20)])
def test_multiplication(a, b, product):
    assert a * b == product


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
       1 / 0
