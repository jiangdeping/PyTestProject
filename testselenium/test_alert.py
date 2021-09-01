# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/1 15:06
from testselenium.base import Base
from selenium.webdriver import ActionChains
from time import sleep
class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag=self.driver.find_element_by_id("draggable")
        drop=self.driver.find_element_by_id("droppable")

        action=ActionChains(self.driver)
        action.click_and_hold(drag).release(drop).perform()
        # action.drag_and_drop(drag,drop).perform()
        sleep(2)
        print("点击alert")
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)