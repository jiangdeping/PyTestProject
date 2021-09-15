# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/15 14:18
from appium.webdriver.common.mobileby import MobileBy

from test_appium.app.page.base_page import BasePage
from test_appium.app.page.member_invite import MemberInvite

class AddressList(BasePage):
    def add_member(self):
        # UiSelector = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))'
        # self._driver.find_element_by_android_uiautomator(UiSelector).click()
        self._driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return MemberInvite(self._driver)