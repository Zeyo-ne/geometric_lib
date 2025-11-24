import unittest
from figures.rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 4), 12)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4), 14)
