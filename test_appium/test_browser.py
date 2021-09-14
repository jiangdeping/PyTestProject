# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/9 16:05
from time import sleep

from appium import webdriver
class TestBrowser:
    def setup(self):
        desiredcaps = {}
        desiredcaps["platformName"] = "android"
        desiredcaps["deviceName"] = "emulator-5554"
        desiredcaps["noReset"] = True
        desiredcaps["chromedriverExecutable"]="C:\Program Files\Appium\\resources\\app\\node_modules\\appium\\node_modules\\appium-chromedriver\chromedriver\win\chromedriver"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desiredcaps)  # 创建连接，固定写法
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)