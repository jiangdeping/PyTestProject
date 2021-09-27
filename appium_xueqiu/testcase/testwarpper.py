# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/27 10:00
import logging
def extend(func):
    def hello(*args,**kwargs):
        print("hello")
        func(*args,**kwargs)
        print("good bye")
    return hello
@extend
def tmp():

    print("tmp")
@extend
def tmp1():

    print("tmp1")

def test_warpper():
    tmp()
    tmp1()
    # logging.basicConfig(level=logging.INFO)
    logging.log(logging.INFO,"1111")
