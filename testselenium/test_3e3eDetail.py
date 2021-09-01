# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/1 10:37
from testselenium.base import Base
class Test_3e3eDetail(Base):
    def test3e3edetail(self):
        self.driver.get("http://sept.3e3e.cn/product/oscmkac.html")
        result=self.driver.find_elements_by_class_name("relevant-content-item")

        for i in result:
            print(i)