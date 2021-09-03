# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/3 15:50
import shelve

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    _driver=None
    _base_url=""
    def __init__(self,driver:WebDriver=None):
        if driver is None:
            self.option = webdriver.ChromeOptions()
            self.option.add_experimental_option("w3c", False)
            self._driver = webdriver.Chrome(options=self.option)
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)

        else:
            self._driver=driver
        if self._base_url !="":
            self._driver.get(self._base_url)
            db = shelve.open("../../conf/cookies/cookies")
            cookies = db["cookies"]
            for cookie in cookies:
                if "expiry" in cookie.keys():
                    cookie.pop("expiry")
                self._driver.add_cookie(cookie)
            self._driver.get(self._base_url)
            #https://work.weixin.qq.com/wework_admin/frame
    def find(self,by,locator):
        return self._driver.find_element(by,locator)
    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)
    def wait_for_click(self,locator,time=10):
        WebDriverWait(self._driver,time).until(expected_conditions.element_to_be_clickable(locator))
    def wait_for_element(self,conditions,time=10):
        WebDriverWait(self._driver,time).until(conditions)
