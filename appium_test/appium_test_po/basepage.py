# -*- coding: utf-8 -*-
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver