# -*- coding: utf-8 -*-
from selenium import webdriver

from testing_web.page_po.contact_page import ContactPage
#首页
class MainPage:
    def goto_contact_page(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_id("menu_contacts").click()
        #到通讯录页面
        return ContactPage()
