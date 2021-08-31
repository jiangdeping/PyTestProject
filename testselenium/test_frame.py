# -*- coding: utf-8 -*-
# Author:jiang
# 2021/8/31 17:17
from testselenium.base import Base
class TestFrame(Base):

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult") #切换frame
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)