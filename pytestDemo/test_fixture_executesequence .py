# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/30 16:23
import pytest


order=[]

@pytest.fixture(scope="session")
def s1():
    order.append("s1")


@pytest.fixture(scope="module")
def m1():
    order.append("m1")


@pytest.fixture
def f1(f3):
    order.append("f1")


@pytest.fixture
def f3():
    order.append("f3")


@pytest.fixture(autouse=True)
def a1():
    order.append("a1")

@pytest.fixture
def f2():
    order.append("f2")


def test_order(f1,m1,f2,s1):
        assert order == ["s1", "m1", "a1", "f3", "f2", "f1"]