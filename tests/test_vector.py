from BasicGeometry import Vector2D



def test_minus():
    vec1 = Vector2D(1, 2)
    vec2 = Vector2D(3, 5)
    assert vec1 - vec2 == Vector2D(-2, -3)
    vec1 -= vec2
    assert vec1 == Vector2D(-2, -3)


def test_add():
    vec1 = Vector2D(1, 2)
    vec2 = Vector2D(3, 5)
    assert vec1 + vec2 == Vector2D(4, 7)
    vec1 += vec2
    assert vec1 == Vector2D(4, 7)


def test_dot():
    vec1 = Vector2D(1, 2)
    vec2 = Vector2D(3, 5)
    assert vec1.dot(vec2) == 13.0


def test_cross():
    vec1 = Vector2D(1, 2)
    vec2 = Vector2D(3, 5)
    assert vec1.cross(vec2) == -1.0
