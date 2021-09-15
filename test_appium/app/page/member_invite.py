# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/15 14:20
from appium.webdriver.common.mobileby import MobileBy

from test_appium.app.page.base_page import BasePage

class  MemberInvite(BasePage):
    def addmember_by_manul(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from test_appium.app.page.contact_add import ContactAdd
        return ContactAdd(self._driver)
    # def get_toast(self):
    #     element=self._driver.find_element(MobileBy.XPATH,"//*[contains(@text,'添加成功')]")
    #     # element=self._driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']")
    #     print(element.text)
    #     return element.text
