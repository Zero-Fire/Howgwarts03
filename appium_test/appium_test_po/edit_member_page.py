# -*- coding: utf-8 -*-
#添加编辑成员界面，编辑完成后，保存，再返回选择手东添加成员界面

class EditMemberPage():
    def edit_member(self):
        from appium_test.appium_test_po.add_member_page import AddMembrePage
        return AddMembrePage()
