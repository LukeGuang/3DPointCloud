"""
STL模型的结构体
"""

from PrimaryStruct import STLFile


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

    @ListTri.setter
    def ListTri(self, ListTri):
        self._ListTri = ListTri

    @staticmethod
    def ReadSTL(strPath):
        """
        从二进制文件中解析STL模型

        :param strPath: 文件路径
        :return: STL模型
        """
        List_TriSlice = STLFile.LoadBrinary(strPath)
        return STLModel(List_TriSlice)
