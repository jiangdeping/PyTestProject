# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/7 11:27
from appium import webdriver
desiredcaps={}
desiredcaps["platformName"]="android"
desiredcaps["deviceName"]="127.0.0.1:7555"
desiredcaps["appPackage"]="com.xueqiu.android"
desiredcaps["appActivity"]=".view.WelcomeActivityAlias"
desiredcaps["noReset"]=True
desiredcaps["dontStopAppOnReset"]=True #首页启动的时候不停止app
desiredcaps["skipDeviceInitialization"]=True #跳过安装权限设置等操作





# desiredcaps={
#   "platformName": "android",
#   "deviceName": "127.0.0.1:7555",
#   "appPackage": "com.xueqiu.android",
#   "appActivity": ".view.WelcomeActivityAlias",
#   "noReset": True #不需要初始化
# }
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desiredcaps) #创建连接，固定写法
driver.implicitly_wait(20)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("阿里巴巴")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]")
el3.click()


driver.back()#返回到上一个页面
driver.quit()
