from src.calculator import plus, minus, divide, multiply


def test_plus():
    answer = plus(1, 2)
    assert answer == 3


def test_minus():
    answer = minus(2, 2)
    assert answer == 0


def test_divide():
    answer = divide(4, 2)
    assert answer == 2


def test_divide_with_zero():
    answer = divide(4, 0)
    assert answer == 0


def test_multiply():
    answer = multiply(4, 2)
    assert answer == 8
