"""
三维空间点
"""
import math
from Commonstruct.Point2D import POINT2D


class POINT3D:
    __slots__ = ('_x', '_y', '_z')

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """
        初始化点坐标

        :param x: X坐标
        :param y: Y坐标
        :param z: Z坐标
        """
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, other):
        if isinstance(other, POINT3D):
            return POINT3D(self._x + other.x, self._y + other.y, self._z + other.z)
        elif isinstance(other, int):
            return POINT3D(self._x + other, self._y + other, self._z + other)
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, POINT3D):
            return POINT3D(self._x - other.x, self._y - other.y, self._z - other.z)
        elif isinstance(other, int):
            return POINT3D(self._x - other, self._y - other, self._z - other)
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, int) and other != 0:
            return POINT3D(self._x / other, self._y / other, self._z / other)
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, int):
            return POINT3D(self._x * other, self._y * other, self._z * other)
        else:
            return None

    def __eq__(self, other):
        return isinstance(other, POINT3D) and self._x == other.x and self._y == other.y and self._z == other.z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    @z.setter
    def z(self, z):
        self._z = z

    @staticmethod
    def norm(pt):
        """
        计算点pt到原点的距离

        :param pt: 输入的点
        :return: 点到原点的距离
        """
        return math.sqrt(pt.x * pt.x + pt.y * pt.y + pt.z * pt.z)

    @staticmethod
    def toPoint(other):
        """
        输入list类型的实例，转化为Point3D类型的实例

        :param other: 1*3 list实例
        :return: Point3D类型的实例
        """
        if len(other) == 3:
            return POINT3D(other[1], other[2], other[3])
        else:
            return None

    def toPoint2D(self):
        return POINT2D(self.x, self.y)

    def __str__(self):
        return '[%.4f, %.4f, %.4f]' % (self._x, self._y, self._z)


if __name__ == "__main__":
    pass
