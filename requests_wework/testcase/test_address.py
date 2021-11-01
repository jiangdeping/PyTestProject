# -*- coding: utf-8 -*-
# Author:jiang
# 2021/11/1 16:43
from requests_wework.api.address import Address
class TestAddress:
    def setup(self):
        self.address=Address()
    def test_create(self):
        print(self.address.create("zhangsan222","zhangsan002","13899888111"))
    def test_update(self):
        print(self.address.update("zhangsan222","zhangsan003","13899888132"))
    def test_delete(self):
        print(self.address.delete("zhangsan222"))