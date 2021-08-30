# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/30 17:27
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def test_selenium():
    dirver=webdriver.Chrome()
    dirver.get("https://www.baidu.com/")
