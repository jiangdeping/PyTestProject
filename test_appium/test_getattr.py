# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/9 10:18
# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/7 11:27
from appium import webdriver
import pytest

from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestGetAttr:
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
        pass
        # self.driver.quit()
    @pytest.mark.skip
    def test_get_attr(self):
        search_ele=self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")

        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))


if __name__=="__main__":
    pytest.main()
