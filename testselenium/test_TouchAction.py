# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/31 15:08
from selenium import webdriver
from selenium.webdriver import TouchActions
from time import sleep
class TestTouchAction():
    def setup(self):
        option=webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver=webdriver.Chrome(options=option)
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com/")
        el=self.driver.find_element_by_id("kw")
        el_search=self.driver.find_element_by_id("su")
        el.send_keys("selenium测试")
        action=TouchActions(self.driver)
        action.tap(el_search)  #单击操作
        action.scroll_from_element(el,0,10000) #执行滑动操作
        action.perform()
        sleep(3)