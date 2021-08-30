# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/24 15:47
#type hints 类型提示
from decimal import getcontext
class Calc:
    #def add(self, a: int, b: int) -> int:
    def add(self,a,b):
        result=a+b
        result=round(result,2) #保留2位小数
        return result
    def div(self, a, b):
        return a / b
calc=Calc()
print(calc.add(0.1,2.2))