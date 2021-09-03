# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/3 11:06
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_main.page.base_page import BasePage

class AddMember(BasePage):
    def add_member(self):
        # sendkeys
        self.find(By.ID,"username").send_keys("张三")
        self.find(By.ID,"memberAdd_english_name").send_keys("ZS")
        self.find(By.ID, "memberAdd_acctid").send_keys("zhangsan")
        self.find(By.ID, "memberAdd_phone").send_keys("18623044309")
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
    def get_member(self):
        self.wait_for_click(By.CSS_SELECTOR,".ww_checkbox")
        elements=self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        members=[element.get_attribute("title") for element in elements]
        return members
    def update_page(self):
        content:str=self.finds(By.CSS_SELECTOR,'')