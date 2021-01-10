# -*- coding: utf-8 -*-
import pytest
import yaml

from testing_web.page_po.mian_page import MainPage

with open ("data_member.yaml") as f:
    data = yaml.safe_load(f)
class TestLogin:

    def setup(self):
        #实例化主页，方便调用，才能调用
        self.main = MainPage()
    def teardown(self):
        pass
    #数据参数化，传参

    # @pytest.mark.parametrize("name,id,email",[('张三','zhangsan','zhangsan@qq.com')])
    @pytest.mark.parametrize("name,id,email",data['member'])
    def test_login(self,name,id,email):
        # name = "张三"
        # id  = "zhangsan"
        # email = "12312@qq.com"
        namelist=self.main.goto_contact_page().click_add_member().add_member(name,id,email).get_member()
        assert name in namelist
    @pytest.mark.parametrize("name,id,email",data['member'],ids=data['key'])
    def test_login_1(self,name,id,email):
        namelist_1=self.main.goto_add_member().add_member(name,id,email).get_member()
        assert name in namelist_1