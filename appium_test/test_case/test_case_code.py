# -*- coding: utf-8 -*-
from appium_test.appium_test_po.app import App

class TestCode():
    def setup(self):
        self.app = App()
    def teardown(self):
        pass
        # self.app.stop()
    def test_case(self):
        ele_toat = self.app.start().goto_main().goto_address_list().click_member().click_add_member().edit_member().estimate()
        assert "添加成功" == ele_toat
