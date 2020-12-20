# -*- coding: utf-8 -*-
from testing_web.page_po.mian_page import MainPage
class TestLogin:

    def setup(self):
        #实例化主页，方便调用，才能调用
        self.main = MainPage()
    def teardown(self):
        pass
    def test_login(self):
        self.main.goto_contact_page().click_add_member().add_member()
