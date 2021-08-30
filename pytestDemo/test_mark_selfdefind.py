# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/26 13:55
import pytest
@pytest.mark.search
def test_search():
    print("test search1")

@pytest.mark.search
def test_search2():
    print("test search2")

@pytest.mark.search
def test_search3():
    print("test search3")

@pytest.mark.login
def test_login1():
    print("test login1")

@pytest.mark.login
def test_login2():
    print("test login2")

if __name__=="__main__":
    pytest.main()