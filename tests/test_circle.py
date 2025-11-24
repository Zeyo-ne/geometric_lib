import unittest
from figures.circle import area, perimeter
import math

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), math.pi, places=5)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi, places=5)
