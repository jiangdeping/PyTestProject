# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/26 9:58
import sys
from python.calc import Calc
from testing.python_pytest import steps
import pytest,yaml
#
@pytest.mark.parametrize("data1,data2,expect",yaml.safe_load(open('../datas/add.yaml')))
def test_add(data1,data2,expect):
    steps1=steps()
    for step in steps1:
        print(f"step===>",{step})
        if "add"== step:
            result=Calc().add(data1,data2)
        elif "add1"==step:
            result = Calc().add(data1, data2)
        print(result)
        assert expect==result
#参数化，前面两个变量，后面是对应的数据
@pytest.mark.parametrize("data1,data2,expect",[(3,3,6),(4,7,11),(12,11,33),(0.1,0.2,0.3)])
def test_sum(data1,data2,expect):
    # calc=Calc()
    result=Calc().add(data1,data2)
    print(result)
    #eval  将字符串str当做有效的表达式来求值，并返回结果
    assert expect==result

#参数组合
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[8,4,7])
def test_foo(x,y):
    print(f"测试数据组合x:{x},y:{y}")


#方法名作为参数
user_data=["Tome","Jerry"]
@pytest.fixture(scope="module")
def login_r(request):
    #接受并传递参数
    user=request.param
    print(f"登录用户:{user}")
    return user

#indirect=True,可以把传过来的参数当函数执行
@pytest.mark.parametrize("login_r",user_data,indirect=True)
def test_login(login_r):
    a=login_r
    print(f"测试用例中login的返回值：{a}")
    assert a != ""


#@pytest.mark.skip("此次测试不执行登录")
#判断满足什么条件不执行
@pytest.mark.skipif(sys.platform =="win32",reason="不在win3上执行")
#indirect=True,可以把传过来的参数当函数执行
@pytest.mark.parametrize("login_r",user_data,indirect=True)
def test_login(login_r):
    a=login_r
    print(f"测试用例中login的返回值：{a}")
    assert a != ""
if __name__=="__main__":
    pytest.main("-v -s")