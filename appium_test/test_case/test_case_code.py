# -*- coding: utf-8 -*-
import yaml

from appium_test.appium_test_po.app import App
import pytest
with open ("data.yaml",encoding="gbk") as f:
    data = yaml.safe_load(f)["add"]
class TestCode():
    def setup(self):
        self.app = App()
    def teardown(self):
        self.app.stop()
        # self.app.stop()
    @pytest.mark.parametrize('name,gender,mail',data)
    def test_case(self,name,gender,mail):
        ele_toat = self.app.start().goto_main().goto_address_list().click_member().\
            click_add_member().edit_member(name,gender,mail).estimate()
        assert "添加成功" == ele_toat

    def delete_member(self):
        pass