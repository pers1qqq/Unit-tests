import unittest
from geometric_lib import square


class SquareTestCase(unittest.TestCase):
    def test_area_usual(self):
        """Площадь квадрата со стороной 4 = 16"""
        res = square.area(4)
        self.assertEqual(res, 16)

    def test_area_zero(self):
        """Площадь при стороне 0 = 0"""
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_perimeter_usual(self):
        """Периметр квадрата со стороной 4 = 16"""
        res = square.perimeter(4)
        self.assertEqual(res, 16)


if __name__ == "__main__":
    unittest.main()