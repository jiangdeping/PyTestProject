# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/25 17:08
import pytest

def test_case1(login):
    print("test case1:login")
def test_case2():
    print("test case2:not login")
def test_case3(login):
    print("test case3:login")
if __name__=="__main__":
    pytest.main()