# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/30 15:54
#yield +函数 =生成器
def provider():
    for i in range(5):
        print("before")
        yield i #生成器， return i+暂停，并记住上一步操作
        print("after")
p=provider()
print(next(p))
print(next(p))
print(next(p))