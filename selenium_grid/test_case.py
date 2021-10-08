# -*- coding: utf-8 -*-
# Author:jiang
# 2021/10/8 14:05
# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/7 11:27
from appium import webdriver
import pytest
import os
class TestSearch:
    def setup(self):
        desiredcaps = {}
        desiredcaps["platformName"] = "android"
        desiredcaps["udid"] =os.getenv("udid",None) #未设置udid，默认取devices列表的第一个设备
        #desiredcaps["udid"] ="127.0.0.1:7555"  # 未设置udid，默认取devices列表的第一个设备
        desiredcaps["appPackage"] = "com.xueqiu.android"
        desiredcaps["appActivity"] = ".view.WelcomeActivityAlias"
        desiredcaps["noReset"] = True
        desiredcaps["dontStopAppOnReset"] = True  # 首页启动的时候不停止app
        desiredcaps["skipDeviceInitialization"] = True  # 跳过安装权限设置等操作
        self.driver = webdriver.Remote("http://192.168.1.189:4444/wd/hub", desiredcaps)  # 创建连接，固定写法
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_serarch(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        self.driver.back()

# if __name__=="__main__":
#     pytest.main()
