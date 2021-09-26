# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/26 14:41
from selenium.webdriver.common.by import By

from testpageobject.page.app import BasePage
class Main(BasePage):
    def goto_search(self):
        self.steps('../page/main.yaml')
    def goto_windows(self):
        self.find(By.ID,"com.xueqiu.android:id/post_status").click()
        self.steps('../page/main.yaml')


