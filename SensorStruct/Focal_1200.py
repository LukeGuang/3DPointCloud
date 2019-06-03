"""
Focal 1200 型号参数
"""
from numpy import *
from Commonstruct import Line3D
from Commonstruct import Point3D


class Focal_1200:
    def __init__(self):
        """
        Focal_1200内部参数初始化

        1. 激光线宽度
            Optical profile length = 11.26 mm
        2. 点间隔
            Pixel size X = 0.0055 mm
        3. Y向最小间隔
            Pixel size Y = 0.025 mm
        4. Z向精度
            Z-resolution = 0.00055 mm
        5. 工作距离
            Stand-off distance = 16.16 mm
        6. 景深
            景深（DOF），是指在摄影机镜头或其他成像器前沿能够取得清晰图像的成像所测定的被摄物体前后距离范围。
            Z-range = 2.8
        7.
            Max slope of object = ±20 deg
        """
        self.pixel_size_x = 0.0055
        self.pixel_num_x = 2048
        self.pixel_size_y = 0.025
        self.z_resolution = 0.00055
        self.stand_off_distance = 16.16
        self.z_range = 2.8
        self.max_slope = 20
        self.location = Point3D()  # 传感器的安装位置
        self.mounting_method = array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])  # 传感器的安装方式(传感器坐标系与世界坐标系一致)
        self.Fix_Posture = Point3D()

    def Fix(self, Fix_Location, mounting_method, Fix_Posture):
        self.location = Fix_Location
        self.mounting_method = mounting_method
        self.Fix_Posture = Fix_Posture

    def Trigger(self):
        """
        触发函数

        :return:
        """
        List_Laser = []
        for i in range(self.pixel_num_x):
            origin = Point3D()
            origin.x = i * self.pixel_num_x
            origin.y = 0
            origin.z = self.location.z
