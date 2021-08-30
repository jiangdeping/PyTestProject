# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/25 17:14
import pytest
@pytest.fixture()
def login():
    print("this login function")

#作用域：module 是在模块执行之前执行，模块之后执行
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield
    print("执行teardown")
    print("关闭浏览器")

def pytest_configure(config):
    marker_list=["search","login"]#标签名集合
    for markers in marker_list:
        config.addinivalue_line("markers",markers)