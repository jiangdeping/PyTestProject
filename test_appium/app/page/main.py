# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/15 14:15
from appium.webdriver.common.mobileby import MobileBy

from test_appium.app.page.addresslist_page import AddressList
from test_appium.app.page.base_page import BasePage

class Main(BasePage):
    def goto_message(self):
        pass
    def goto_addresslist(self):
        self._driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/f1n' and @text='通讯录']").click()

        return AddressList(self._driver)
    def goto_workbench(self):
        pass
    def goto_profile(self):
        pass