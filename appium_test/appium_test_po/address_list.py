# -*- coding: utf-8 -*-
#通讯录页面，点击添加成员，进入添加成员页面
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium_test.appium_test_po.add_member_page import AddMembrePage
from appium_test.appium_test_po.basepage import BasePage


class Addresslist(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    def click_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                     'new UiScrollable(new UiSelector().'
        #                     'scrollable(true).instance(0)).'
        #                     'scrollIntoView(new UiSelector().'
        #                     'text("添加成员").instance(0));').click()
        self.find_scroll_and_click("添加成员")
        return AddMembrePage(self.driver)