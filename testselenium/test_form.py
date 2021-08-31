# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/31 15:26
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

class TestForm():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_form(self):
        self.driver.get("http://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("username")
        self.driver.find_element_by_id("user_password").send_keys("password")
        ele=self.driver.find_element_by_xpath('//*[@id="user_remember_me"]')
        action = ActionChains(self.driver)
        action.click(ele).perform()#ele.click()点击被拦截，用此方法代替
        # self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        sleep(3)