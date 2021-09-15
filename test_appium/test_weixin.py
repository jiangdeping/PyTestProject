# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/15 9:39
from appium import webdriver
import pytest
#
# driver.back()#返回到上一个页面
# driver.quit()
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Testweixin:
    def setup(self):
        desiredcaps = {}
        desiredcaps["platformName"] = "android"
        desiredcaps["udid"] = "77c1ca380903" #未设置udid，默认取devices列表的第一个设备
        desiredcaps["appPackage"] = "com.tencent.wework"
        desiredcaps["appActivity"] = ".launch.LaunchSplashActivity"
        desiredcaps["noReset"] = True
        desiredcaps["dontStopAppOnReset"] = True  # 首页启动的时候不停止app
        desiredcaps["skipServerInstallation"] = True
        desiredcaps["skipDeviceInitialization"] = True  # 跳过安装权限设置等操作
        self.driver = webdriver.Remote("http://127.0.0.1:4727/wd/hub", desiredcaps)  # 创建连接，固定写法
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_addcontract(self):
        print("添加联系人")
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/f1n' and @text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/bf6").send_keys("李四")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/ge0").send_keys("18633328898")
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/ana').click()
        # s=self.driver.find_element(MobileBy.XPATH,"//*[@contains(@text,'添加成功')]")
