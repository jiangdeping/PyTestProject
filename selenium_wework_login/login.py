# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/1 16:16
from time import sleep

from selenium.webdriver.common.by import By
from selenium_wework_login.register import Register
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import TouchActions

class Login:
    def __init__(self,driver:WebDriver):
        self._driver=driver
    def scanf(self):
        pass
    def goto_register(self):
        element=self._driver.find_element(By.CSS_SELECTOR,'.login_stage_title_text')
        sleep(1)
        action = TouchActions(self._driver)
        action.scroll_from_element(element,0,4000).perform()
        self._driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return Register(self._driver)
