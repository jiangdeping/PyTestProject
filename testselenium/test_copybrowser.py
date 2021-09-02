# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/2 17:12
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestCopyBrowser():
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.find_element(By.ID,"menu_contacts").click()
        sleep(3)