# -*- coding: utf-8 -*-
# Author:jiang
# 2021/11/1 17:39
from  requests_wework.api.base_api import BaseApi
class WeWork(BaseApi):
    def get_token(self,secret):
        corpid = "ww6cbf9f5776d6a5e9"
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret":secret,
            }
        }
        return self.send(**data)["access_token"]
