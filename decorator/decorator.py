# -*- coding: utf-8 -*-
# Author:jiang
# 2021/10/28 10:15
# class ClassDemo:
#     def __init__(self,func):
#         self.func=func
#     def __call__(self,*args,**kwargs):
#         print(f'runing {self.func.__name__}')
#         self.func()
#         print(f'end {self.func.__name__}')
#
# @ClassDemo
# def foo():
#     print("do something")
import time
#带有固定参数的装饰器
def deco(f):
    def wrapper(a,b):
        start_time = time.time()
        f(a,b)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" %execution_time )
    return wrapper

@deco
def f1(a,b):
    print("be on")
    time.sleep(1)
    print("result is %d"%(a+b))

#无固定参数的装饰器
def deco(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        f(*args,**kwargs)

        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" %execution_time )
    return wrapper

@deco
def f2(a,b):
    print("be on")
    time.sleep(1)
    print("result is %d"%(a+b))

@deco
def f3(a,b,c):
    print("be on")
    time.sleep(1)
    print("result is %d"%(a+b+c))

