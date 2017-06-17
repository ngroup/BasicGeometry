from tiny2d import Polygon


def test_initialize():
    polygon = Polygon([(1, 1), (1, 2), (2, 3), (3, 2.6), (2.5, 0)])
    assert polygon.vertices == [(1, 1), (1, 2), (2, 3), (3, 2.6), (2.5, 0)]

def test_translate():
    polygon = Polygon([(1, 1), (1, 2), (2, 3)])
    polygon_tranlated = polygon.translate((2, 2))
    assert polygon_tranlated.vertices == [(3, 3), (3, 4), (4, 5)]

def test_contains():
    polygon = Polygon()
    polygon.add_vertex((1, 1))
    polygon.add_vertex((1, 2))
    polygon.add_vertex((2, 3))
    polygon.add_vertex((3, 2.6))
    polygon.add_vertex((2.5, 0))
    assert polygon.contains((1.5, 1.5))
    assert (not polygon.contains((0, 1.5)))
    assert (not polygon.contains((1.6, 3.1)))
