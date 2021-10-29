# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/27 10:13
import logging

import allure
from appium.webdriver.common.mobileby import MobileBy

def handle_black(func):
    logging.basicConfig(level=logging.INFO)
    def warpper(*args,**kwargs):
        from appium_xueqiu.page.base_page import BasePage
        _black_list = [
            (MobileBy.ID,"com.xueqiu.android:id/action_search"),
            (MobileBy.XPATH, "//*[@text='确定']"),
            (MobileBy.XPATH, "//*[@text='下次再说']"),
            (MobileBy.XPATH, "//*[@text='确认']"),
        ]
        _max_num = 3
        _error_num = 0
        instance:BasePage=args[0]
        try:
            logging.info("run: "+func.__name__+"\n args:\n"+repr(args[1:])+"\n"+repr(kwargs))
            element=func(*args,**kwargs)
            _error_num=0
            instance._driver.implicitly_wait(10)
            return element
        except Exception as e:
            instance.screenshot("tmp.png")
            with open("tmp.png","rb")as f:
                content=f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG) #截图
            logging.info("element not found,handle black list ")
            instance._driver.implicitly_wait(1)
            if _error_num>_max_num:
                raise e
            _error_num+=1
            for ele in _black_list:
                elelist=instance.finds(*ele)
                if len(elelist)>0:
                    elelist[0].click()
                    return warpper(*args,**kwargs)
            raise e
    return warpper


