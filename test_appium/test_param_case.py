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
    def setup_class(self):#每个类级别执行一次
        print("setup_class")
        desiredcaps = {}
        desiredcaps["platformName"] = "android"
        desiredcaps["deviceName"] = "127.0.0.1:7555"
        desiredcaps["appPackage"] = "com.xueqiu.android"
        desiredcaps["appActivity"] = ".view.WelcomeActivityAlias"
        desiredcaps["noReset"] = True
        desiredcaps["dontStopAppOnReset"] = True  # 首页启动的时候不停止app
        desiredcaps["skipDeviceInitialization"] = True  # 跳过安装权限设置等操作
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desiredcaps)  # 创建连接，固定写法
        self.driver.implicitly_wait(10)
    def setup(self):
        print("setup")#调一次case执行一次

    def teardown(self):
        print("teardown")
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()
    def teardown_class(self):
        print("teardown_class")
        self.driver.quit()
    @pytest.mark.parametrize('searchkey,type,price',[
           ('alibaba','BABA',180),
           ('xiaomi','01810',22)
       ])
    def test_search(self,searchkey,type,price):
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click()
        # locator = (MobileBy.XPATH, f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        #current_price = float(self.driver.find_element(*locator).text)
        price_element=self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current_price=float(price_element.text)
        expect_price=price
        print(current_price)
        assert_that(current_price,close_to(expect_price,current_price*0.1))
if __name__ == "__main__":
    pytest.main()