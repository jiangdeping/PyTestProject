# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/26 14:34
from appium.webdriver.webdriver import WebDriver
import yaml
from selenium.webdriver.common.by import By

class BasePage:
    _driver:WebDriver
    _black_list=[(By.ID,"com.xueqiu.android:id/iv_action_back")]
    def __init__(self,driver:WebDriver=None):
        self._driver=driver
    def find(self,locator,value):
        try:
            element=self._driver.find_element(locator,value)
            return element
        except:
            for black in self._black_list:
                elements=self._driver.find_elements(*black)
                if len(elements)>0:
                    elements[0].click()
                    break
            return self.find(locator,value)
    def click(self,locator,value):
        return self.find(locator,value).click()
    def steps(self,path):
        with open(path) as f:
            steps=yaml.safe_load(f)
        element=None
        for step in steps:
            if "by" in step.keys():
                element=self.find(step["by"],step["locator"])
            if "action" in step.keys():
                action=step["action"]
                if action=="click":
                    element.click()

