# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/3 11:02
import shelve
from time import sleep
from selenium.webdriver.common.by import By
from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage

class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_index_add_member(self):
        self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMember(self._driver)
    def goto_member_add_member(self):
        self.find(By.ID,"menu_contacts").click()
        self.wait_for_click((By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)'),10)
        # def wait_add_member(x):
        #     elements_len=len(self.finds(By.CSS_SELECTOR,"#username"))
        #     if elements_len<=0:
        #         self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        #     return elements_len>0

        # self.wait_for_element(wait_add_member)
        self.find(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        #.js_has_member>div:nth-child(1) .js_add_member
        #.js_has_member>div:nth-child(1)>a:nth-child(2)
        return AddMember(self._driver)