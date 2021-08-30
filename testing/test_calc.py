# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/24 15:49
import unittest
import sys
print(sys.path)
sys.path.append("..") #添加上一级路径
print(sys.path)
from  python.calc import Calc

class TestCal(unittest.TestCase):
    def test_add_1(self):
        self.calc=Calc()
        result=self.calc.add(1,2)
        self.assertEqual(3,result)
        print(result)
unittest.main()