# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/13 10:36
from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions

class TestMobileMutual:
    def setup(self):
        desiredcaps = {}
        desiredcaps["platformName"] = "android"
        desiredcaps["deviceName"] = "127.0.0.1:7555"
        # desiredcaps["deviceName"] ="77c1ca380903"
        # #emulator-5554
        desiredcaps["appPackage"] = "com.xueqiu.android"
        desiredcaps["appActivity"] = ".view.WelcomeActivityAlias"
        desiredcaps["noReset"] = True
        desiredcaps["dontStopAppOnReset"] = True  # 首页启动的时候不停止app
        desiredcaps["skipDeviceInitialization"] = True  # 跳过安装权限设置等操作
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desiredcaps)  # 创建连接，固定写法
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_Mobile_Mutual(self):
        self.driver.make_gsm_call("13833881128",GsmCallActions.CALL)#模拟打电话
        self.driver.send_sms("13988989989","hello world")#模拟发短信
        self.driver.set_network_connection()#切换网络连接
        self.driver.get_screenshot_as_file()#保存截图