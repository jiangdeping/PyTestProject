# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/31 16:03
import sys
print(sys.path)
sys.path.append("..") #添加上一级路径
from time import sleep
import pytest
from selenium.webdriver import ActionChains
from testselenium.base import Base
class TestWindowsHandler(Base):
    def test_windowsHandler(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("s-top-loginbtn").click()
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        ele_uesrname=self.driver.find_element_by_id("TANGRAM__PSP_4__userNameWrapper")
        ele_phone = self.driver.find_element_by_id("TANGRAM__PSP_4__phone")
        action = ActionChains(self.driver)
        action.move_to_element(ele_uesrname).send_keys("alber2021")
        # action.send_keys_to_element(ele_uesrname,"alber123520").perform()
        action.send_keys_to_element(ele_phone, "18623099388")
        action.perform()
        sleep(2)
        self.driver.switch_to.window(window_handles[0]) #切换窗口
        sleep(1)
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("alber123520")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("jiang123456")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(2)
if __name__ == '__main__':
    pytest.main("-v -s")