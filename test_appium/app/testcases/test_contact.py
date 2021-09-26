# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/15 14:35
from test_appium.app.page.app import App
class TestContact:
    def setup(self):
        self.app=App()
        self.main=self.app.start().main()
    def test_addcontact(self):
        element=self.main.goto_addresslist().add_member().addmember_by_manul().\
            input_name().input_phone().click_save()
        assert "成功" in element.get_toast()
    def test_repeataddcontact(self):
        element=self.main.goto_addresslist().add_member().addmember_by_manul().\
            input_name().input_phone().click_save()
        assert "已存在于通讯录"in element.get_repeat1()