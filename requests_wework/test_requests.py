# -*- coding: utf-8 -*-
# Author:jiang
# 2021/11/1 11:03
import random
import re

import pytest
import requests
from filelock import FileLock

@pytest.fixture(scope="session")
def test_token():
    res=None
    # while FileLock('session.lock'): #解决xdist只执行一次test_token()，进行加锁，锁住的内容只执行一次
    corpid="ww6cbf9f5776d6a5e9"
    corsecret="7gqpOvV5-NwiXckj6aibBSMQ5h9C_YbV2kYteqIUUfo"
    res=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corsecret}")
    print("get_token")
    return res.json()["access_token"]


def test_get(userid,test_token):
    USERID=userid
    res=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={USERID}")
    return res.json()

def test_create(userid,name,mobile,test_token):
    data ={
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1],
    }
    res=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}",json=data)
    return res.json()

def test_update(userid,name,mobile,test_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
    }
    res=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}",json=data)
    return res.json()

def test_delete(userid,test_token):
    res=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
    return res.json()
def test_crate_data():
    # data =[(str(random.randint(10000,99999)),"zhangsan"+str(str(random.randint(100,999))),(str(random.randint(13811110000,13811119999)))) for x in range(10)]
    data=[('zhangsan'+str(x),"张三"+str(x),"138%08d"%x)for x in range(5)]
    return data
@pytest.mark.parametrize("userid,name,mobile",test_crate_data())
def test_all(userid,name,mobile,test_token):
    try:
        #可能发生创建失败
        assert "created" == test_create(userid,name,mobile,test_token)["errmsg"]
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            print('str--->',e.__str__())
            re_userid=re.findall(":(.*)\\'",e.__str__())[0]
            print(f"re_userid:{re_userid}")
            assert "deleted" == test_delete(re_userid,test_token)['errmsg']
            assert 60111 == test_get(userid,test_token)['errcode']
            assert "created" == test_create(userid, name, mobile,test_token)["errmsg"]
    #可能发生userid不存在异常
    assert name ==test_get(userid,test_token)["name"]
    assert "updated" ==test_update(userid,"xxxxx",mobile,test_token)['errmsg']
    assert "xxxxx" == test_get(userid,test_token)["name"]
    assert "deleted" == test_delete(userid,test_token)['errmsg']
    assert 60111 ==test_get(userid,test_token)['errcode']