# -*- coding: utf-8 -*-
# Author:jiang
# 2021/11/1 16:36
import requests
class BaseApi:
    def send(self,**data):
        print(data)
        return requests.request(**data).json() #加** 解析成多个参数