# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/1 13:48
from testselenium.base import Base
from time import sleep
import pytest

class TestJs(Base):
    @pytest.mark.skip
    def test_js_scoll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element=self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)
        for  code in ['return document.title','return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))
    def test_datatime(self):
        self.driver.get("https://www.12306.cn/index/")
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
        self.driver.execute_script('a=document.getElementById("train_date");a.value="2021-12-12"')
        sleep(5)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))