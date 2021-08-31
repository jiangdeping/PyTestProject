# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/30 17:35
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
class TestHogwards():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)#隐示等待
    def teardown(self):
        self.driver.quit()
    def test_hogwards(self):
        self.driver.get("http://testerhome.com/")
        self.driver.find_element(By.XPATH,'//*[@class="nav-link"]').click()
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("testerhome管理委员会").click()

        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(()))
