from files import calculate as c

def test_add_function():
    assert c.add_numbers(4, 8) == 12
    assert c.add_numbers(-2, 2) == 0
    assert c.add_numbers(4, -10) == -6
