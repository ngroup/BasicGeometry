# -*- coding: utf-8 -*-
import unittest
from whichside.polygon import Polygon
from whichside.line import Line


class TestPolygon(unittest.TestCase):
    def setUp(self):
        pass

    def test_polygon1(self):
        polygon = Polygon()
        polygon.add_vertex(1, 1)
        polygon.add_vertex(1, 2)
        polygon.add_vertex(2, 3)
        polygon.add_vertex(3, 2.6)
        polygon.add_vertex(2.5, 0)

        self.assertTrue(polygon.contains(1.5, 1.5))
        self.assertFalse(polygon.contains(0, 1.5))
        self.assertFalse(polygon.contains(1.6, 3.1))

    def test_polygon2(self):
        polygon = Polygon()
        polygon.add_vertex(1, 1)
        polygon.add_vertex(1, 2)
        polygon.add_vertex(1.5, 1.5)
        polygon.add_vertex(3, 2.6)
        polygon.add_vertex(2.5, 0)

        self.assertFalse(polygon.contains(1.5, 1.6))
        self.assertFalse(polygon.contains(0, 1.5))
        self.assertTrue(polygon.contains(1.3, 1.7))


class TestLine(unittest.TestCase):
    def setUp(self):
        pass

    def test_line1(self):
        line = Line([1, 1], [2, 2.5])
        self.assertFalse(line.is_clockwise_to_point(1, 0))
        self.assertTrue(line.is_clockwise_to_point(1.5, 3.0))

    def test_line2(self):
        line = Line([1.0, 1.0], [-2.0, -2.5])
        self.assertFalse(line.is_clockwise_to_point(0.0, 2.0))
        self.assertTrue(line.is_clockwise_to_point(0, -2))


if __name__ == '__main__':
    unittest.main()
