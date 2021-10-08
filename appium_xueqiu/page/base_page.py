# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/15 15:00
import inspect
import json
import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from appium_xueqiu.page.wrapper import handle_black

class BasePage:
    _params={}
    logging.basicConfig(level=logging.INFO)
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
    def set_implicitly(self,time):
        self._driver.implicitly_wait(time)
    def screenshot(self,name):
        self._driver.save_screenshot(name)
    def finds(self,locator,value:str=None):
        elements:list #返回值是list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements
    @handle_black
    def find(self,locator,value:str=None):
        # logging.info(locator)
        # logging.info(value)
        element:WebElement
        if isinstance(locator,tuple):
            element=self._driver.find_element(*locator)
        else:
            element=self._driver.find_element(locator,value)
        return element
    @handle_black
    def find_and_get_text(self,locator,value:str=None):
        element:WebElement
        if isinstance(locator,tuple):
            element_text=self._driver.find_element(*locator).text
        else:
            element_text=self._driver.find_element(locator,value).text
        return element_text
    def steps(self,path):
        with open(path,encoding="utf-8") as f:
            name=inspect.stack()[1].function #获取当前被调用的函数名
            steps=yaml.safe_load(f)[name]
        #yaml文件内容进行参数化
        raw=json.dumps(steps)
        for key,value in self._params.items():
            raw=raw.replace(f'${{{key}}}',value) #f语法  {{}}转义 -> 代表{}  {key}:变量名称
            #raw = raw.replace('${'+key+'}', value) 与上面等价
        steps=json.loads(raw)
        for step in steps:
            if "action" in step.keys():
                action=step["action"]
                if "click"==action:
                    self.find(step["by"], step["locator"]).click()
                if "send"==action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "len > 0" ==action:
                    eles=self.finds(step["by"],step["locator"])
                    return len(eles)>0
