# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/26 17:31
from appium_xueqiu.page.app import App

class TestSearch():
    def setup(self):
        self.search=App().start().main().goto_market().goto_search()
    def test_search(self):
        self.search.search()
        assert  self.search.is_choose()