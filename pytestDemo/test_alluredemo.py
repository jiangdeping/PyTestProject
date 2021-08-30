# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/26 15:33
import pytest
def test_success():
    assert True
def test_failure():
    assert False
def test_skip():
    pytest.skip("for a reason")
def test_broken():
    raise Exception("oops")