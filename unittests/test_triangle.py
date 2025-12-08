import unittest
import geometric_lib.triangle as triangle

import os
import sys

CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


class TriangleTestCase(unittest.TestCase):
    def test_area_usual(self):
        """Площадь треугольника: 10 * 5 / 2 = 25"""
        res = triangle.area(10, 5)
        self.assertEqual(res, 25)

    def test_perimeter_3_4_5(self):
        """Периметр треугольника со сторонами 3, 4, 5 = 12"""
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)


if __name__ == "__main__":
    unittest.main()