import unittest
import geometric_lib.square as square

import os
import sys

CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


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