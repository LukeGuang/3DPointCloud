"""
用于仿真程序从stl中获取所需要的数据，根本思想为计算三角面片与激光的交点
引入噪声的概念，每个交点的z坐标都会加入一点噪声
"""
from Commonstruct import *


def main():
    STL_Path = r"E:\项目\项目文件\3D玻璃50066\伯恩\模型\伯恩#P30.stl"
    stl_1 = STLModel.ReadSTL(STL_Path)  # type STLModel


if __name__ == "__main__":
    main()
