"""
STL模型的结构体
"""

from Commonstruct import TriangleSlice, Point3D, Triangle


class STLModel:
    def __init__(self, ListTri=None):
        """
        STL模型初始化
        :param ListTri: 三角片List
        """
        self._ListTri = ListTri  # type: list

    @property
    def ListTri(self):
        return self._ListTri

    @staticmethod
    def ReadSTL(strPath):
        """
        从文件中解析STL模型

        :param strPath: 文件路径
        :return: STL模型
        """
        TriangleList = []
        with open(strPath, 'r', encoding='utf-8') as f:
            fileLines = f.readlines()[1:-1]  # 去除文件头、文件尾
        for i in range(0, len(fileLines), 7):
            tempVertex = []
            # 解析法向量
            tempFacet = Point3D.toPoint(list(map(float, fileLines[i].split(' ')[2:4])))
            # 解析三个顶点
            tempVertex.append(Point3D.toPoint(list(map(float, fileLines[i + 2].split(' ')[1:4]))))
            tempVertex.append(Point3D.toPoint(list(map(float, fileLines[i + 3].split(' ')[1:4]))))
            tempVertex.append(Point3D.toPoint(list(map(float, fileLines[i + 4].split(' ')[1:4]))))
            temp = TriangleSlice(tempFacet, Triangle.toTriangle(tempVertex))
            TriangleList.append(temp)
        return STLModel(TriangleList)
