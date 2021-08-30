# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/26 12:05
import pytest
@pytest.fixture(params=[1, 2, 3, "linda"])
def test_data(request):
    return request.param
def test_one(test_data):
    print(f"test data:{test_data}")
