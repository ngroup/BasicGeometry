import tiny2d as t2d

class Line(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_clockwise_to_point(self, x, y):
        '''
        Compute the cross product of (AB) X (AP), where P is (x, y)
        '''
        ab = (self.end[0] - self.start[0], self.end[1] - self.start[1])
        ap = (x - self.start[0], y - self.start[1])
        cp = ab[0] * ap[1] - ap[0] * ab[1]

        return cp > 0


class InfiniteLine:
    '''
    An Infinite Line: a * x + b * y + c = 0
    '''
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._n_vector = self.n_vector
        self._reference = self.reference

    @property
    def n_vector(self):
        return t2d.Vector2D(self._a, self._b)

    @property
    def reference(self):
        '''
        get a reference point on line
        '''
        if self._a == 0:
            return t2d.Vector2D(0, -1 * sel._c / self._b)
        else:
            return t2d.Vector2D(-1 * self._c / self._a, 0)

    def reflect(self, p):
        p = t2d.Vector2D(*p)
        rp = p - self._reference
        u = rp.project_to(self._n_vector)
        new_p = p - 2 * u
        return new_p

    def distance(self, p):
        p = t2d.Vector2D(*p)
        rp = p - self._reference
        u = rp.project_to(self._n_vector)
        return u.length
