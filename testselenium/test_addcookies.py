# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/2 17:12
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class addCookies():
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        # self.driver.find_element(By.ID,"menu_contacts").click()
        cookies = [
            {'domain': '.qq.com', 'expiry': 1630575450, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/',
                             'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False,
                                                             'name': 'wxpay.vid', 'path': '/', 'secure': False,
                                                             'value': '1688856778235188'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                'secure': False, 'value': '1970325094486112'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False,
                                                                'name': 'wwrtx.vid', 'path': '/', 'secure': False,
                                                                'value': '1688856778235188'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                'value': 'O5YnVp_wRozptMT6MCjosbb6OnD93lUf0dUbnIUooGlpQmGz-m106iU-0yD_aY8kC4ezbzzlMsvkfO2wELrHxoFTqnqSstNPPRrhYT-NnuP2EY-FB0o4MT3w3JEzrYNfAAkzoa_d4KqJa_xbZfe-H1l9YWQv0Pw65wTpg-CGyIQnHcfCQ7Zbcrl48FDK3vvgQFX2eXXgTpLvFSReFhDFXtv07zJ51Z-csu3xU8s7_Lz5DRy6kw5kdwyo6_-i-yX_JVnIebpvIRD5dPyYt1oIPQ'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
                'value': 'a2708547'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False,
                                       'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                       'value': '1630574667'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
                                                                'name': 'wwrtx.refid', 'path': '/', 'secure': False,
                                                                'value': '5335552141535134'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
                'value': 'HNBfTVTOtgyCYE0TFxj2OpqrmLDlDrbf7Fo2RadkVw1CadMKE4gqIFIxtG9hjKCd'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
                'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid',
                                'path': '/', 'secure': False, 'value': '4900818855'}, {'domain': '.work.weixin.qq.com',
                                                                                       'expiry': 1662110666,
                                                                                       'httpOnly': False,
                                                                                       'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d',
                                                                                       'path': '/', 'secure': False,
                                                                                       'value': '1630484361,1630570744,1630574667'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
                'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1693647390, 'httpOnly': False, 'name': '_ga',
                                     'path': '/', 'secure': False, 'value': 'GA1.2.106452766.1630484362'}, {
                'domain': '.work.weixin.qq.com', 'expiry': 1662020360, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
                'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
                                                              'name': 'wwrtx.logined', 'path': '/', 'secure': False,
                                                              'value': 'true'}, {'domain': '.qq.com',
                                                                                 'expiry': 1630661790.2223,
                                                                                 'httpOnly': False, 'name': '_gid',
                                                                                 'path': '/', 'secure': False,
                                                                                 'value': 'GA1.2.1046495699.1630484362'}, {
                'domain': '.work.weixin.qq.com', 'expiry': 1633167393, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
                'path': '/', 'secure': False, 'value': 'zh'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)