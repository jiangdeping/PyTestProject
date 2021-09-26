# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/26 14:52


from testpageobject.page.app import App
class TestMain:
    def test_main(self):
        app=App()
        app.start().main().goto_search()
    def test_windows(self):
        app = App()
        app.start().main().goto_windows()
