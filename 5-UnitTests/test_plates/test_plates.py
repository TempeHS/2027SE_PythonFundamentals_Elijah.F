from plates import is_valid


def test_length():
    assert is_valid("CS50") == True


def test_alnum():
    assert is_valid("ABC123") == True


def test_no_leading_zero():
    assert is_valid("CBD100") == True


def test_all_letters():
    assert is_valid("ABEFPO") == True
