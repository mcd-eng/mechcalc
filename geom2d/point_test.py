import unittest

from geom2d.point import Point
from geom2d.vector import Vector

class TestPoint(unittest.TestCase):

    def test_distance_to(self):
        p = Point(1,2)
        q = Point(4,6)
        expected = 5
        actual = p.distance_to(q)

        self.assertAlmostEqual(expected, actual)

    def test_add(self):
        p = Point(1,2)
        q = Point(2,3)
        expected = Vector(3,5)
        actual = p + q

        self.assertEqual(expected, actual)

    def test_sub(self):
        p = Point(5,5)
        q = Point(2,3)
        expected = Point(3,2)
        actual = p - q

        self.assertEqual(expected, actual)
