from BasicGeometry.polygon import Polygon


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

