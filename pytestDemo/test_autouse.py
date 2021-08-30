# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/25 17:08
import pytest
#autouse=True 将自动应用到每一条测试用例
@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")
def test_case1(open):
    print("test case1")
def test_case2(open):
    print("test case2")
def test_case3(open):
    print("test case3")
if __name__=="__main__":
    pytest.main()