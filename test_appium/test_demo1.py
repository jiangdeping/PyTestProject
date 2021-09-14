# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/7 11:27
from appium import webdriver
import pytest
#
# driver.back()#返回到上一个页面
# driver.quit()
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Testappniumdemo:
    def setup(self):
        desiredcaps = {}
        desiredcaps["platformName"] = "android"
        desiredcaps["udid"] = "77c1ca380903" #未设置udid，默认取devices列表的第一个设备
        desiredcaps["appPackage"] = "com.xueqiu.android"
        desiredcaps["appActivity"] = ".view.WelcomeActivityAlias"
        desiredcaps["noReset"] = True
        desiredcaps["dontStopAppOnReset"] = True  # 首页启动的时候不停止app
        desiredcaps["skipDeviceInitialization"] = True  # 跳过安装权限设置等操作
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desiredcaps)  # 创建连接，固定写法
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_serarch(self):
        """
        1.打开需求app
        2.点击搜索输入框
        3.向搜索框里面输入“阿里巴巴”
        4.在搜索结果选择“阿里巴巴”进行点击
        5.获取阿里巴巴的股价，并判断这支价格>200
        :return:
        """

        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        elements=self.driver.find_elements_by_id("com.xueqiu.android:id/current_price")
        for element in elements:
            print(element.text)
        # assert current_price<200
        self.driver.back()
    def test_attr(self):
        element=self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        print(element.text)
        print(element.location)
        print(element.size)
        if element.is_enabled():
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            ele=self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            ele_display=ele.get_attribute("displayed")
            print(ele_display)
            if ele_display =="true":
                print("搜索成功")
            else:
                print("搜索失败")
    def test_xpath(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price=self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"股票价格是:{current_price}")
        assert  float(current_price)<200
        self.driver.back()
    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        locator=(MobileBy.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        current_price=self.driver.find_element(*locator).text
        print(f"股票价格是:{current_price}")
        assert  float(current_price)<200
        self.driver.back()
    def test_uiautomator(self):
        """
        点击我的，进入到个人信息页面
        点击登录，进入登录页面
        输入用户名，输入密码
        点击登录
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        loc_textContains = 'new UiSelector().textContains("密码登录")'
        self.driver.find_element_by_android_uiautomator(loc_textContains).click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()

        # self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/rl_login']//*[@text='帐号密码登录']").click()

    def test_uiautomator_scroll_find_element(self):
        """
        滚动查找元素
        :return:
        """
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        UiSelector='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("李一恩的投资组合").instance(0))'
        self.driver.find_element_by_android_uiautomator(UiSelector).click()
if __name__=="__main__":
    pytest.main()
