# -*- coding: utf-8 -*-
#微信主页，点击通讯录进入通讯录页面
from appium_test.appium_test_po.address_list import Addresslist


class MainPage():
    def goto_address_list(self):
        return Addresslist()
