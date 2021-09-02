# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/31 16:05
from selenium import webdriver
import os
class Base():
    def setup(self):
        browser=os.getenv("browser")
        if browser=="firefox":
            self.driver=webdriver.Firefox()
        else:
            self.driver=webdriver.Chrome()
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐示等待
    def teardown(self):
        self.driver.quit()