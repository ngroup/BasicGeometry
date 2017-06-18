from tiny2d import Line, InfiniteLine


# class TestLine():
#     def setUp(self):
#         pass

#     def test_line1(self):
#         line = Line([1, 1], [2, 2.5])
#         self.assertFalse(line.is_clockwise_to_point(1, 0))
#         self.assertTrue(line.is_clockwise_to_point(1.5, 3.0))

#     def test_line2(self):
#         line = Line([1.0, 1.0], [-2.0, -2.5])
#         self.assertFalse(line.is_clockwise_to_point(0.0, 2.0))
#         self.assertTrue(line.is_clockwise_to_point(0, -2))

def test_InfiniteLine_distance():
    line = InfiniteLine(1, 0, -5)
    assert line.distance((0, 0)) == 5

def test_InfiniteLine_reflect():
    line = InfiniteLine(1, 0, -5)
    assert line.reflect((0, 0)) == (10, 0)
    assert line.reflect((10, 0)) == (0, 0)
