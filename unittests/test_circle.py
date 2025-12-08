import unittest
import math
import geometric_lib.circle as circle


class CircleTestCase(unittest.TestCase):
    def test_perimeter_zero_radius(self):
        """Периметр при r = 0 должен быть 0"""
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_unit_radius(self):
        """Периметр при r = 1 должен быть 2π"""
        res = circle.perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi, places=7)

    def test_area_unit_radius(self):
        """
        Ожидаем, что в circle.py есть функция area(r) = π r^2.
        Этот тест сначала упадёт, пока ты её не реализуешь.
        """
        res = circle.area(1)
        self.assertAlmostEqual(res, math.pi, places=7)


if __name__ == "__main__":
    unittest.main()