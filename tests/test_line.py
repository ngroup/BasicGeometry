from tiny2d.line import Line


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

