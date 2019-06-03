"""
三维空间点
"""
import math
import numpy


class Vector3D:
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
        if isinstance(other, Vector3D):
            return Vector3D(self._x + other.x, self._y + other.y, self._z + other.z)
        elif isinstance(other, int):
            return Vector3D(self._x + other, self._y + other, self._z + other)
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self._x - other.x, self._y - other.y, self._z - other.z)
        elif isinstance(other, int):
            return Vector3D(self._x - other, self._y - other, self._z - other)
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, int) and other != 0:
            return Vector3D(self._x / other, self._y / other, self._z / other)
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector3D(self._x * other, self._y * other, self._z * other)
        elif isinstance(other, numpy.ndarray) and other.shape == (3, 3):
            tempVector = numpy.array(self.toList())
            print(tempVector)
            print(other)
            # 这里有点问题
            return numpy.dot(tempVector, other)
        else:
            return None

    def __eq__(self, other):
        return isinstance(other, Vector3D) and self._x == other.x and self._y == other.y and self._z == other.z

    def toList(self):
        return [self._x, self._y, self._z]

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
    def norm(vector):
        """
        计算向量的模

        :param vector: 输入的向量
        :return: 向量的模
        """
        return math.sqrt(vector.x * vector.x + vector.y * vector.y + vector.z * vector.z)

    @staticmethod
    def toPoint(other):
        """
        输入list类型的实例，转化为Point3D类型的实例

        :param other: 1*3 list实例
        :return: Point3D类型的实例
        """
        if len(other) == 3:
            return Vector3D(other[0], other[1], other[2])
        else:
            return None

    def __str__(self):
        return '[%.4f, %.4f, %.4f]' % (self._x, self._y, self._z)


if __name__ == "__main__":
    v = Vector3D(1, 0, 0)
    m = numpy.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
    print(v * m)
