"""
STL文件类
"""
import struct
from Commonstruct import Point3D, TriangleSlice


def LoadBrinary(strPath):
    """
    读取STL二进制文件

    :param strPath:
    :return:
    """
    List_TriangleSlice = []
    with open(strPath, 'rb') as f:
        f.read(80)  # 流出80字节，文件名
        temp = f.read(4)  # 流出4字节，文件中结构体的数量
        count = struct.unpack('I', temp)[0]
        for i in range(count):
            List_TriangleSlice.append(TriangleSliceRead(f))
    return List_TriangleSlice


def TriangleSliceRead(f):
    """
    从字节流中读取三角片

    :param f:
    :return:
    """
    triSlice = TriangleSlice()
    triSlice.facet = PointRead(f)
    triSlice.vertex.vertex1 = PointRead(f)
    triSlice.vertex.vertex2 = PointRead(f)
    triSlice.vertex.vertex3 = PointRead(f)


def PointRead(f):
    """
    从字节流中读取点(32位无符号整数，每次读取4个字节)

    :param f:
    :return:
    """
    point = Point3D()
    point.x = struct.unpack('f', f.read(4))[0]
    point.y = struct.unpack('f', f.read(4))[0]
    point.z = struct.unpack('f', f.read(4))[0]
    return point


if __name__ == '__main__':
    filepath = r"E:\下载\伯恩#P30.stl"
    LoadBrinary(filepath)
