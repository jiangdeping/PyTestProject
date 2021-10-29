# -*- coding: utf-8 -*-
# Author:jiang
# 2021/10/28 10:58
import math
class Circle:
    def __init__(self,radius): #园的半径
        self.radius=radius

    @property
    def area(self):
        return math.pi*self.radius**2

    @property
    def perimeter(self):
        return 2*math.pi*self.radius

circle=Circle(10)
print(circle.radius)
print(circle.area)
print(circle.perimeter)