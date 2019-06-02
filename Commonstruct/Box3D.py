"""
Box结构体
"""
from Commonstruct.Point3D import POINT3D


class Box3D:

    def __init__(self, maxPoint, minPoint):
        """

        Box初始化，两个点构造一个与世界坐标系平行的Box
        :param maxPoint:
        :param minPoint:
        """
        if isinstance(maxPoint, POINT3D) and isinstance(minPoint, POINT3D):
            self._max = maxPoint
            self._min = minPoint
        else:
            self._max = None
            self._min = None

    def translate(self, pt):
        """
        平移操作

        :param pt: 平移向量
        :return:
        """
        if isinstance(pt, POINT3D):
            self._max += pt
            self._min += pt

    def isNULL(self):
        """
        判断Box是否有效

        :return:
        """
        return self._min is None and self._max is None

    def isEmpty(self):
        """
        判断Box是否为空

        :return:
        """
        return self._max == self._min

    def centerPoint(self):
        """
        计算Box的中心点

        :return:
        """
        return (self._max + self._min) / 2

    def volumn(self):
        return (self._max.x - self._min.x) * (self._max.y - self._min.y) * (self._max.z - self._min.z)

    def dimX(self):
        return self._max.x - self._min.x

    def dimY(self):
        return self._max.y - self._min.y

    def dimZ(self):
        return self._max.z - self._min.z

    @property
    def max(self):
        return self._max

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, minPoint):
        self._min = minPoint

    @max.setter
    def max(self, maxPoint):
        self._max = maxPoint
