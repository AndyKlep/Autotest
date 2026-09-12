import unittest
from main import ostatok

class TestOstatok(unittest.TestCase):
    def test_ostatok(self):
        self.assertEqual(ostatok(10, 2), 0)
        self.assertEqual(ostatok(7, 3), 1)
        self.assertEqual(ostatok(19, 2), 17)

class TestOstatok2(unittest.TestCase):
    def test_divide_by_zero(self):
        self.assertRaises(ValueError, ostatok, 6, 0)

print(ostatok(6, 5))


if __name__ == '__main__':
    unittest.main()