# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/15 14:14

from appium import webdriver

from appium_xueqiu.page.main import Main
from test_appium.app.page.base_page import BasePage

class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"
    def start(self):
        if self._driver==None:
            desiredcaps = {}
            desiredcaps["platformName"] = "android"
            desiredcaps["udid"] = "77c1ca380903"  # 未设置udid，默认取devices列表的第一个设备
            desiredcaps["appPackage"] = self._package
            desiredcaps["appActivity"] = self._activity
            desiredcaps["noReset"] = True
            desiredcaps["dontStopAppOnReset"] = True  # 首页启动的时候不停止app
            desiredcaps["skipServerInstallation"] = True
            desiredcaps["skipDeviceInitialization"] = True  # 跳过安装权限设置等操作
            self._driver = webdriver.Remote("http://127.0.0.1:4727/wd/hub", desiredcaps)  # 创建连接，固定写法
        else:
            self._driver.launch_app()#直接启动应用
        self._driver.implicitly_wait(3)
        return self
    def restart(self):
        pass
    def stop(self):
        pass
    def main(self) ->Main(): #返回Main()类型
        return Main(self._driver)