# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/26 17:18
from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage

class Search(BasePage):
    def search(self,name):
        self._params["name"]=name
        self.steps('../page/search.yaml')
    def add(self,name):
        self._params["name"] = name
        self.steps('../page/search.yaml')
    def is_choose(self,name):
        self._params["name"] = name
        return self.steps('../page/search.yaml')
    def reset(self,name):
        self._params["name"] = name
        return self.steps('../page/search.yaml')
    def cancel(self,name):
        self._params["name"] = name
        return self.steps('../page/search.yaml')