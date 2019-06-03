from Commonstruct import Point3D


class Line3D:
    def __init__(self, origin=Point3D(), direction=Point3D(1, 0, 0)):
        self._origin = origin
        self._direction = direction

    @property
    def origin(self):
        return self._origin

    @property
    def direction(self):
        return self._direction

    @origin.setter
    def origin(self, origin):
        self._origin = origin

    @direction.setter
    def direction(self, direction):
        self._direction = direction
