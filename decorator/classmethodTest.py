# -*- coding: utf-8 -*-
# Author:jiang
# 2021/10/28 11:06
class A():
    number=10
    @classmethod
    def get_a(cls):
        print('这是类本身',cls)
        print('这是类属性',cls.number)
A.get_a()