
import importlib
import Point
importlib.reload(Point)
from Point import Point



p = Point(-5, -5)
p2 = Point(-5, -7)
p.distance(p2)

import unittest


class TestPoint(unittest.TestCase):

    def test_same_points_distance_is_zero(self):
        x = 0
        y = 0
        p = Point(x, y)
        p2 = Point(x, y)

        self.assertEqual(0, p.distance(p2))

    def test_minus_points_distance_is_absolute(self):
        x = 0
        y = 0
        p = Point(x, y)
        p2 = Point(x, y)

        self.assertEqual(0, p.distance(p2))



def main():

    testPoint = TestPoint()
    testPoint.test_same_points_distance_is_zero()




if __name__ == "__main__":
    main()
