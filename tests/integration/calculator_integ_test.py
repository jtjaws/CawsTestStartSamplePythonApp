from src.calculator import plus, minus, divide, multiply, get_hello


def test_integration():
    answer = plus(1, 2) + minus(2, 2) + divide(4, 2) + multiply(4, 2)
    response = get_hello("CAWS.Test")

    result = response + str(answer)

    assert result == "hello CAWS.Test13.0"
