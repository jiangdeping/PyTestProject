# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/31 14:09
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys

class TestActionChains():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        # element_click=self.driver.find_element_by_xpath("/html/body/form/input[3]")
        # element_doubleclick = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        # element_rightclick = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        element_click=self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action=ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        action.perform()
        time.sleep(1)

    @pytest.mark.skip
    def test_moveto(self):
        self.driver.get("https://www.baidu.com/")
        element=self.driver.find_element_by_id("s-usersetting-top")
        action=ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        time.sleep(2)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element=self.driver.find_element_by_id("dragger")
        drop_element=self.driver.find_element_by_xpath("/html/body/div[2]")
        action=ActionChains(self.driver)
        # action.drag_and_drop(drag_element,drop_element).perform()
        action.click_and_hold(drag_element).release(drop_element).perform()#拖拽
        time.sleep(3)
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        element=self.driver.find_element_by_xpath("/html/body/label[1]/input")
        element.click()
        action=ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("Tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()
        time.sleep(2)
