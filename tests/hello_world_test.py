from src.hello_world import get_hello


def test_answer():
    response = get_hello("CAWS.Test")
    assert response == "hello CAWS.Test"


def test_answer_covering_branch():
    response = get_hello("DEV")
    assert response == "hello super DEV"
