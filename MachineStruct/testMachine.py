"""
测试机台的参数
"""
from numpy import *

# 世界坐标系(笛卡尔坐标系/右手坐标系)
Matrix_World = eye(3, 3)
# 世界坐标系转化为机台坐标系
Matrix_Machine = Matrxi_Wrold_to_Machine = array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])

"""
1. 以世界坐标系为基准
2. 建立机台坐标系
"""
