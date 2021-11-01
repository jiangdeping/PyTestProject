# -*- coding: utf-8 -*-
# Author:jiang
# 2021/11/1 14:26
import requests
def test_token():
    corpid="ww6cbf9f5776d6a5e9"
    corsecret="7gqpOvV5-NwiXckj6aibBSMQ5h9C_YbV2kYteqIUUfo"
    res=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corsecret}")
    return res.json()["access_token"]

def test_create():
    data={
        "name": "重庆研发中心",
        "parentid": 1,
    }
    res=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}",json=data)
    print(res.json())

def test_update():
    data={
       "id": 2,
       "name": "成都研发中心",
    }
    res=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}",json=data)
    print(res.json())
def test_delete():
    res=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id=2")
    print(res.json())

def test_get():
    res=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token()}&id=1")
    print(res.json())