# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/26 16:07
import pytest,yaml
from selenium.webdriver.common.by import By

class TestMain:
    @pytest.mark.parametrize("value1,value2",yaml.safe_load(open('../test_case/test_main.yaml')))
    def test_parametrize(self,value1,value2):
        print(value1,value2)
        y=yaml.safe_load(open('../page/configguration.yaml'))
        print(y)
        s = y['caps']['udid']
        print(s)
        s=yaml.safe_load(open('../page/main.yaml'))
        print(s)
        s=yaml.safe_load(open('../test_case/test_main.yaml'))
        print(s)
    def test_parms(self):
        vars=[(1,2),(3,4)]
        def sum(a,b):
            return a+b
        for i in vars:
            s=sum(*i)
            print(s)