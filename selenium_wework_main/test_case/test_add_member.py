# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/3 11:19
from time import sleep

from selenium_wework_main.page.main import Main

class TestAddMember:
    def setup(self):
        self.main=Main()
    def test_index_addmember(self):
        add_member=self.main.goto_index_add_member()
        add_member.add_member()
        assert  "张三" in add_member.get_member()
    def test_member_addmember(self):
        add_member = self.main.goto_member_add_member()
        add_member.add_member()
        assert "张三" in add_member.get_member()
