"""
三角形
"""


class Triangle:
    def __init__(self, vertex1=None, vertex2=None, vertex3=None):
        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._vertex3 = vertex3

    @staticmethod
    def toTriangle(pointList):
        if len(pointList) == 3:
            pt1, pt2, pt3 = pointList
            return Triangle(pt1, pt2, pt3)
        else:
            return None

    @property
    def vertex1(self):
        return self._vertex1

    @vertex1.setter
    def vertex1(self, vertex1):
        self._vertex1 = vertex1

    @property
    def vertex2(self):
        return self._vertex2

    @vertex2.setter
    def vertex2(self, vertex2):
        self._vertex2 = vertex2

    @property
    def vertex3(self):
        return self._vertex3

    @vertex3.setter
    def vertex3(self, vertex3):
        self._vertex3 = vertex3

