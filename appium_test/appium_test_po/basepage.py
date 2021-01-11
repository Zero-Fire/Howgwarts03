# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver
    #封装查找元素方法
    def find(self,locator):
        return self.driver.find_element(*locator)

    #封装 查找元素并点击方法
    def find_and_click(self,locator):
        self.find(locator).click()

    #封装滚动查找元素并点击元素
    def find_scroll_and_click(self,text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));')
        self.find_and_click(ele)

    #封装获取toast方法
    def find_and_get_test(self,locator):
        return self.find(locator).text