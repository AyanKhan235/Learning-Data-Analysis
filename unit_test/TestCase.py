import unittest
import math 
import circle
class TestCircle(unittest.TestCase):
    def test_area1(self):
        self.assertEqual(circle.circle_area(1), math.pi)
    def test_area_0(self):
        self.assertEqual(circle.circle_area(0),0)