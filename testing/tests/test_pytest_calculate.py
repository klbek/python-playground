from files import calculate as c

def test_add_function():
    assert c.add_numbers(4, 8) == 12
    assert c.add_numbers(-2, 2) == 0
    assert c.add_numbers(4, -10) == -6

def test_is_even():
    assert c.is_even(4) is True
    assert c.is_even(0) is True
    assert c.is_even(-6) is True
    assert c.is_even(-1) is False
    assert c.is_even(3) is False
    