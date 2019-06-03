"""
三角面片结构
"""

from Commonstruct import Point3D
from Commonstruct import Triangle


class TriangleSlice:
    def __init__(self, facet=Point3D(), vertex=Triangle()):
        """
        三角面片初始化函数

        :param facet: 法向量
        :param vertex: 顶点(3个)
        """
        self._facet = facet
        self._vertex = vertex

    @property
    def vertex(self):
        return self._vertex
