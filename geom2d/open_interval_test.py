import unittest
from geom2d.open_interval import OpenInterval

class TestInterval(unittest.TestCase):

    def test_compute_overlap(self):
        
        i1 = OpenInterval(1,5)
        i2 = OpenInterval(2,4)
        expected = i1.compute_overlap_with(i2)
        print(expected)
