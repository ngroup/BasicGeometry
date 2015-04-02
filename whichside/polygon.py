# -*- coding: utf-8 -*-


class Polygon(object):
    def __init__(self):
        self.vertices = []

    def add_vertex(self, x, y):
        self.vertices.append((x, y))

    def contains(self, x, y):
        """Determine if a point is inside a given polygon or not
        Uses the 'Ray Casting' algorithm
        http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html
        """

        n = len(self.vertices)
        inside = False

        p1x, p1y = self.vertices[0]
        for i in range(n + 1):
            p2x, p2y = self.vertices[i % n]
            if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x):
                if p1y != p2y:
                    c = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if p1x == p2x or x <= c:
                    inside = not inside
            p1x, p1y = p2x, p2y

        return inside
