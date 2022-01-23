# -*- coding: utf-8 -*-
# Author:jiang
# 2021/11/1 16:28
import requests

from requests_wework.api.base_api import BaseApi
from requests_wework.api.wework import WeWork


class Address(BaseApi):
    def __init__(self):
        corpsecret = "7gqpOvV5-NwiXckj6aibBSMQ5h9C_YbV2kYteqIUUfo"
        self.token = WeWork().get_token(corpsecret)

    def create(self, userid, name, mobile):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {"access_token": self.token},
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1],
            },
        }

        return self.send(**data)

    def update(self, userid, name, mobile):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {"access_token": self.token},
            "json": {"userid": userid, "name": name, "mobile": mobile},
        }
        return self.send(**data)

    def delete(self, userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {"access_token": self.token, "userid": userid},
        }
        return self.send(**data)
