# -*- coding: utf-8 -*-
from appium_test.appium_test_po.main_page import MainPage
from appium import webdriver

class TestCode():
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.driver.quit()
    def test_case(self):
        self.main.goto_address_list().click_member().click_add_member().edit_member().estimate()

