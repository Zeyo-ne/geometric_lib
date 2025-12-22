import unittest
from figures.triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_3_4_5(self):
        # треугольник со сторонами 3, 4, 5
        self.assertAlmostEqual(area(3, 4, 5), 6)

    def test_perimeter_3_4_5(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_area_equilateral(self):
        # равносторонний треугольник
        a = 10
        expected_area = (a**2 * 3**0.5) / 4
        self.assertAlmostEqual(area(a, a, a), expected_area)

    def test_perimeter_equilateral(self):
        self.assertEqual(perimeter(5, 5, 5), 15)

    def test_area_float_values(self):
        self.assertAlmostEqual(area(2.5, 3.5, 4), 4.353, places=3)

    def test_big_numbers(self):
        a = 10**6
        expected_area = (a**2 * 3**0.5) / 4
        self.assertAlmostEqual(area(a, a, a), expected_area)
