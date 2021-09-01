# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/1 14:42
from testselenium.base import Base
from time import sleep
class TestFile(Base):
    def test_image_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("stfile").send_keys("D:\\pythonTest\\PyTestProject\\testselenium\\jianzhu.jpg")
        sleep(5)
