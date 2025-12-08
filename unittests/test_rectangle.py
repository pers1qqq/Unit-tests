import unittest
import geometric_lib.rectangle as rectangle

import os
import sys

CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


class RectangleTestCase(unittest.TestCase):
    def test_area_usual(self):
        """Площадь прямоугольника со сторонами 3 и 4 = 12"""
        res = rectangle.area(3, 4)
        self.assertEqual(res, 12)

    def test_area_zero_side(self):
        """Площадь с нулевой стороной должна быть 0"""
        res = rectangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_perimeter_usual(self):
        """Периметр прямоугольника 2x3 = 2 * (2 + 3) = 10"""
        res = rectangle.perimeter(2, 3)
        self.assertEqual(res, 10)

    def test_perimeter_square_rectangle(self):
        """Периметр квадрата 5x5 = 20"""
        res = rectangle.perimeter(5, 5)
        self.assertEqual(res, 20)


if __name__ == "__main__":
    unittest.main()