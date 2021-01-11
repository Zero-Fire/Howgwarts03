# -*- coding: utf-8 -*-
#微信主页，点击通讯录进入通讯录页面
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from appium_test.appium_test_po.address_list import Addresslist
from appium_test.appium_test_po.basepage import BasePage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    address_ele  = (MobileBy.XPATH,"//*[@text='通讯录']")
    def goto_address_list(self):
        # self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.find_and_click(self.address_ele)
        return Addresslist(self.driver)
