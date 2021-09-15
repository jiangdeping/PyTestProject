# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/15 15:00
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    #弹框处理的定位列表
    _black_list=[
        (MobileBy.XPATH,"//*[@text='确定']"),
        (MobileBy.XPATH, "//*[@text='下次再说']"),
        (MobileBy.XPATH, "//*[@text='确认']"),
    ]
    _max_num=3
    _error_num=0
    def __init__(self,driver:WebDriver = None):
        self._driver=driver
    def find(self,locator,value:str=None):
        element:WebElement
        try:
            if isinstance(locator,tuple):
                element=self._driver.find_element(*locator)
            else:
                element=self._driver.find_element(locator,value)
            #找到之前_error_num归0
            self._error_num=0
            #隐示等待回复原来的等待
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            #出现异常，将隐示等待设置小一点快速处理弹框
            self._driver.implicitly_wait(1)
            if self._error_num>self._max_num:
                raise  e
            self._error_num+=1

            #处理弹框
            for ele in self._black_list:
                elelist=self._driver.find_elements(*ele)
                if len(elelist)>0:
                    elelist[0].click()
                    #处理完成再次查找目标元素
                    return self.find(locator,value)
            raise e