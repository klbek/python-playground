import unittest
from files import calculate as c

class TestCalcFunction(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(c.add_numbers(4, 8), 12)
        self.assertEqual(c.add_numbers(-2, 2), 0)
        self.assertEqual(c.add_numbers(4, -10), -6)

    def test_is_even(self):
        self.assertTrue(c.is_even(4))
        self.assertTrue(c.is_even(0))
        self.assertTrue(c.is_even(-6))
        self.assertFalse(c.is_even(-1))
        self.assertFalse(c.is_even(-3))


# pro spousteni pomoci pytest neni nutne
if __name__ == "__main__":
    unittest.main()

