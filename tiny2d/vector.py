
class Vector2D(tuple):

    def __new__(self, x, y):
        return tuple.__new__(Vector2D, ((x * 1.0, y * 1.0)))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def length2(self):
        x, y = self
        return (x * x + y * y)

    @property
    def length(self):
        return self.length2 ** 0.5

    def __add__(self, other):
        try:
            x, y = self
            ox, oy = other
        except Exception:
            return NotImplemented
        return tuple.__new__(Vector2D, (x + ox, y + oy))

    __iadd__ = __add__

    def __sub__(self, other):
        try:
            x, y = self
            ox, oy = other
        except Exception:
            return NotImplemented
        return tuple.__new__(Vector2D, (x - ox, y - oy))

    __isub__ = __sub__

    def __mul__(self, other):
        """multiply the vector by a scalar
        """
        try:
            x, y = self
            other = float(other)
        except TypeError:
            return NotImplemented
        return tuple.__new__(Vector2D, (x * other, y * other))

    __rmul__ = __imul__ = __mul__

    def __truediv__(self, other):
        """divide the vector by a scalar
        """
        try:
            other = float(other)
        except TypeError:
                return NotImplemented
        return tuple.__new__(Vector2D, (self[0] / other, self[1] / other))

    __itruediv__ = __truediv__

    def __eq__(self, other):
        try:
            return (self[0] == other[0] and self[1] == other[1]
                    and len(other) == 2)
        except (TypeError, IndexError):
            return False

    def __ne__(self, other):
        try:
            return (self[0] != other[0] or self[1] != other[1]
                    or len(other) != 2)
        except (TypeError, IndexError):
            return True

    __hash__ = tuple.__hash__

    def dot(self, other):
        '''
        Compute dot product with another vector
        '''
        x, y = self
        ox, oy = other
        return x * ox + y * oy

    def cross(self, other):
        '''
        Compute cross product with another vector
        '''
        x, y = self
        ox, oy = other
        return x * oy - y * ox

    def project_to(self, other):
        """
        Compute the projection of this vector onto another one.
        """
        other = Vector2D(*other)
        u = self.dot(other) * other / other.length2
        return tuple.__new__(Vector2D, (u[0], u[1]))


class Vector2DArray:
    """
    A wrapper to Vector2D's array
    """
    pass
