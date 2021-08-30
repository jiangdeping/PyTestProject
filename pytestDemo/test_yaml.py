# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/26 14:29
import yaml,pytest
class TestDate:
    @pytest.mark.parametrize(("a","b"), yaml.safe_load(open("../datas/data_1.yaml")))
    def test_data(self,a,b):
        print(a+b)
class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("../datas/env.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境ip地址是：",env["test"])
        elif "dev" in env:
            print("开发正式环境")
            print("开发环境ip地址是：", env["dev"])
    def test_yaml(self):
        print(yaml.safe_load(open("../datas/env.yaml")))
# with open("data.yaml") as f:
#     print(yaml.safe_load(f))
