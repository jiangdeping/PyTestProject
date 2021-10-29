# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/27 10:00
import logging
# def extend(func):
#     def hello(*args,**kwargs):
#         print("hello")
#         func(*args,**kwargs)
#         print("good bye")
#     return hello
# @extend
# def tmp():
#     print("tmp")
# @extend
# def tmp1():
#     print("tmp1")
# def test_warpper():
#     tmp()
#     tmp1()
#     # # logging.basicConfig(level=logging.INFO)
#     # logging.log(logging.INFO,"1111")
# test_warpper()
# from functools import wraps
# def hint(func):
#     @wraps(func)
#     def warpper(*args,**kwargs):
#         print('{} is running'.format(func.__name__))
#         return func(*args,**kwargs)
#     return warpper
# @hint
# def hello():
#     print("hello!")
# hello()
def out_func():
    a=1
    def inner_func(b):
        c=a+b
        print(c)
    return inner_func
func=out_func()
# func(100)
func(100)
out_func()(1000)