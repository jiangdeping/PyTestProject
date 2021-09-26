# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/15 14:22
from appium.webdriver.common.mobileby import MobileBy

from test_appium.app.page.base_page import BasePage
from test_appium.app.page.base_page import BasePage
from test_appium.app.page.member_invite import MemberInvite

class ContactAdd(BasePage):
    def input_name(self):
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/bf6").send_keys("柳少")

        return self
    def input_phone(self):
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/ge0").send_keys("18333328898")

        return self
    def click_save(self):
        self._driver.find_element(MobileBy.ID,'com.tencent.wework:id/ana').click()
        return self
        # from test_appium.app.page.member_invite import MemberInvite
        # return MemberInvite()
    def get_toast(self):
        element=self._driver.find_element(MobileBy.XPATH,"//*[contains(@text,'添加成功')]")
        # element=self._driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        return element.text
    # def get_repeat(self):
    #     element = self._driver.find_element(MobileBy.ID, "com.tencent.wework:id/c0s")
    #     text=element.text
    #     self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/c0w").click()
    #     self._driver.find_element(MobileBy.ID,'com.tencent.wework:id/iza').click()
    #     return text

    def get_repeat1(self):
        ele=self.find(MobileBy.ID, "com.tencent.wework:id/c0s")
        # element = self._driver.find_element(MobileBy.ID, "com.tencent.wework:id/c0s")
        text=ele.text
        # self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/c0w").click()
        self.find(MobileBy.ID,'com.tencent.wework:id/iza').click()
        return text