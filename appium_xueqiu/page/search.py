# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/26 17:18
from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage

class Search(BasePage):
    def search(self):
        self.find(By.ID,'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.find(By.XPATH,'//*[@text="BABA"]').click()
        self.find(By.XPATH,
                  '//*[contains(@resource-id,"ll_stock_item_container")]//*[@text="阿里巴巴"]/../..//*[@text="加自选"]').click()

    def is_choose(self):
        elements=self.finds(By.XPATH, '//*[contains(@resource-id,"ll_stock_item_container")]//*[@text="阿里巴巴"]/../..//'
                            '*[@text="已添加"]')
        return len(elements)>0