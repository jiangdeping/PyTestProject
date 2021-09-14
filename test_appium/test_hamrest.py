# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/9 14:13
from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestHamcrest:
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

    @pytest.mark.skip
    def test_harmcrest(self):
        assert_that(10,equal_to(10))
        assert_that(8,close_to(10,2))
        assert_that("contains some string",contains_string("some"))
    def test_current_price(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        current_price =float (self.driver.find_element(*locator).text)
        print(f"股票价格是:{current_price}")
        expect_price=170
        assert_that(current_price,close_to(expect_price,current_price*0.1))
        self.driver.back()
if __name__ == "__main__":
    pytest.main()