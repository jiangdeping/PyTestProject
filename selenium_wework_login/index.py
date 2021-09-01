# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/1 16:14
from selenium_wework_login.register import Register
from selenium_wework_login.login import Login
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
class Index:
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("w3c", False)
        self._driver =webdriver.Chrome(options=self.option)
        self._driver.maximize_window()
        self._driver.get("https://work.weixin.qq.com/")
    def goto_login(self):
        self._driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return Login(self._driver)
    def goto_register(self):
        element=self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn')
        action=ActionChains
        action.click(element).perform()
        # self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)

