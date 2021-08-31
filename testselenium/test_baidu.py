# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/31 11:26
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
    def test_wait(self):
        # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃茨测试学院")
        # self.driver.find_element(By.ID, "kw").send_keys("霍格沃茨测试学院")
        self.driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("霍格沃茨测试学院")
        self.driver.find_element(By.CSS_SELECTOR, "#su").click()
        self.driver.window_handles