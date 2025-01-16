import unittest
from files import calculate as c

class TestAddFunction(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(c.add_numbers(4, 8), 12)
        self.assertEqual(c.add_numbers(-2, 2), 0)
        self.assertEqual(c.add_numbers(4, -10), -6)

if __name__ == "__main__":
    unittest.main()

