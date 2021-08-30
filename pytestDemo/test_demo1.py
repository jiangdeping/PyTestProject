# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/25 10:09
import pytest
# class TestDemo():
#     def test_one(self):
#         print("执行test_one方法")
#         x='this'
#         assert 'h' in x
#     def test_two(self):
#         print("执行test_two方法")
#         x='hello'
#         assert 'h' in x
#     def test_three(self):
#         print("执行test_three方法")
#         a='hello'
#         b='hello world'
#         assert a in b
# if __name__=='__main__':
#     # pytest.main("-v -x TestDemo")
#     pytest.main(['-v','-s','TestDemo'])

def test_one():
    print("执行test_one方法")
    x='this'
    assert 'h' in x
def test_two():
    print("执行test_two方法")
    x='hello'
    assert 'h' in x
def test_three():
    print("执行test_three方法")
    a='hello'
    b='hello world'
    assert a in b