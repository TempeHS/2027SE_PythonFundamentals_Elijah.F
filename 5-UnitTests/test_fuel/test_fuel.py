from fuel import convert, gauge


def test_convert():
    assert convert("3/4") == 75


def test_empty():
    assert convert("0/3") == 0


def test_gauge():
    assert gauge(75) == "75%"


def test_full():
    assert gauge(100) == "F"
