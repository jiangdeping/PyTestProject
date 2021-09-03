# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/1 17:02
from selenium_wework_login.index import Index

class TestRegister():
    def setup(self):
        self.index=Index()
    def test_register(self):
        # self.index.goto_login().goto_register().register()
        self.index.goto_register().register()