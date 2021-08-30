# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/24 16:
import pytest

from python.calc import Calc
class TestCalc:
    def setup(self):
        self.calc = Calc()
    def test_add(self):
        result=self.calc.add(1,2)
        print(result)
        assert 3==result
    def test_div(self):
        result=self.calc.div(1,2)
        print(result)
        assert 0.5==result
if __name__=="__main__":  #python 入口函数
    pytest.main() #需要传入字符串列表,新版本的字符串类型的参数已废弃。运行需要使用python解释器来执行