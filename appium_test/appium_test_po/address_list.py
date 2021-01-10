# -*- coding: utf-8 -*-
#通讯录页面，点击添加成员，进入添加成员页面
from appium_test.appium_test_po.add_member_page import AddMembrePage


class Addresslist():
    def click_member(self):
        return AddMembrePage()