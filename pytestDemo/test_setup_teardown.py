# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/25 10:32
import pytest

def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")

def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

def test_login():
    print("外部方法")

class TestDemo():
    def setup_class(self):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def setup(self):
        print("setup")

    def teardown_class(self):
        print("teardown_class")

    def teardown_method(self):
        print("teardown_method")

    def test_one(self):
        print("执行test_one方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("执行test_two方法")
        x = 'hello'
        assert 'h' in x

    def test_three(self):
        print("执行test_three方法")
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__ == '__main__':
    pytest.main("-v -s")
