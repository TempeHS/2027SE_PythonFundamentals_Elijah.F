from bank import value


def test_hello():
    assert value("hello") == "$0"


def test_hey():
    assert value("hey") == "$20"


def test_no_greeting():
    assert value("butterfly") == "$100"


def test_uppercase():
    assert value("Hello") == "$0"
