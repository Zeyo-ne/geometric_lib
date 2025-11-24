import unittest
from figures.square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 25)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)
