import unittest
from figures.triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_3_4_5(self):
        # треугольник со сторонами 3, 4, 5
        self.assertAlmostEqual(area(3, 4, 5), 6)

    def test_perimeter_3_4_5(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
