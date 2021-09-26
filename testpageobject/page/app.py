# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/26 14:36
import yaml
from appium import webdriver

from testpageobject.page.base_page import BasePage
from testpageobject.page.main import Main
class App(BasePage):
    _package= "com.xueqiu.android"
    _activity =".view.WelcomeActivityAlias"
    def start(self):
        if self._driver is None:#为空，driver 初始化
            desiredcaps = {}
            desiredcaps["platformName"] = "android"
            desiredcaps["udid"]=yaml.safe_load(open('../page/configguration.yaml'))['caps']['udid']
            print(desiredcaps["udid"])
            # desiredcaps["udid"] = "77c1ca380903"  # 未设置udid，默认取devices列表的第一个设备
            desiredcaps["appPackage"] = self._package
            desiredcaps["appActivity"] = self._activity
            desiredcaps["noReset"] = True
            desiredcaps["dontStopAppOnReset"] = True  # 首页启动的时候不停止app
            desiredcaps["skipDeviceInitialization"] = True  # 跳过安装权限设置等操作
            self._driver = webdriver.Remote("http://127.0.0.1:4727/wd/hub", desiredcaps)  # 创建连接，固定写法
        else:#不为空，直接调用
            self._driver.start_activity(self._package,self._activity)
        self._driver.implicitly_wait(10)
        return self
    def main(self)->Main: #返回Main函数
        return  Main(self._driver)

