# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/27 10:13
from appium.webdriver.common.mobileby import MobileBy

def handle_black(func):
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
            element=func(*args,**kwargs)
            _error_num=0
            instance._driver.implicitly_wait(10)
            return element
        except Exception as e:
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


