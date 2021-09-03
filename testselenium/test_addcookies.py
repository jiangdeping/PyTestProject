# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/2 17:12
import shelve

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

class TestCookies():
    def setup(self):
        # options = Options()
        # options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
    def test_get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(20)
        cookies = self.driver.get_cookies()
        db = shelve.open("../conf/cookies/cookies")
        db["cookies"] = cookies
        db.close()
    def test_load_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        db=shelve.open("../conf/cookies/cookies")
        cookies=db["cookies"]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        db.close()
        sleep(4)