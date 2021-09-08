# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/7 11:27
from appium import webdriver
import pytest
#
# driver.back()#返回到上一个页面
# driver.quit()
from appium.webdriver.common.touch_action import TouchAction

class TestTouchAction:
    def setup(self):
        desiredcaps = {}
        desiredcaps["platformName"] = "android"
        desiredcaps["deviceName"] = "127.0.0.1:7555"
        desiredcaps["appPackage"] = "com.xueqiu.android"
        desiredcaps["appActivity"] = ".view.WelcomeActivityAlias"
        desiredcaps["noReset"] = True
        desiredcaps["dontStopAppOnReset"] = True  # 首页启动的时候不停止app
        desiredcaps["skipDeviceInitialization"] = True  # 跳过安装权限设置等操作
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desiredcaps)  # 创建连接，固定写法
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_touchacction(self):
        action=TouchAction(self.driver)
        window_rect=self.driver.get_window_rect()
        width=window_rect["width"]
        height=window_rect["height"]
        x1=int(width/2)
        y_start=int(height*4/5)
        y_end=int(height*1/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()
if __name__=="__main__":
    pytest.main()
