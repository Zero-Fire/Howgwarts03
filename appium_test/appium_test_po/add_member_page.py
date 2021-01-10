# -*- coding: utf-8 -*-
#添加成员界面，点击手动输入成员进入添加编辑成员界面
from appium_test.appium_test_po.edit_member_page import EditMemberPage


class AddMembrePage():
    def click_add_member(self):
        return EditMemberPage()
    #断言是否添加成功
    def estimate(self):
        pass
