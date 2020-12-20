# -*- coding: utf-8 -*-
from selenium import webdriver

from testing_web.page_po.contact_page import ContactPage

#添加成员页面
class AddMemberPage:
   def add_member(self):
       opt = webdriver.ChromeOptions()
       opt.debugger_address = "127.0.0.1:9222"
       driver = webdriver.Chrome(options=opt)
       driver.implicitly_wait(5)
       driver.find_element_by_id('username').send_keys("张三")
       driver.find_element_by_id("memberAdd_acctid").send_keys("zhangsan")
       driver.find_element_by_id('memberAdd_mail').send_keys("zhangsan@qq.com")
       driver.find_element_by_css_selector('.js_btn_save').click()
       #返回到通讯录页面
       return ContactPage()
