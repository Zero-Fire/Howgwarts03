# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from testing_web.page_po.basepage import BasePage
from testing_web.page_po.contact_page import ContactPage

#添加成员页面
class AddMemberPage(BasePage):
    #参数化
    _ele_name = (By.ID,"username")
    _ele_id = (By.ID,"memberAdd_acctid")
    _ele_email = (By.ID,"memberAdd_mail")
    def add_member(self,name,id,email):
       self.find(*self._ele_name).send_keys(name)
       self.find(*self._ele_id).send_keys(id)
       self.find(*self._ele_email).send_keys(email)
       self.find(By.CSS_SELECTOR,'.js_btn_save').click()
       #返回到通讯录页面
       return ContactPage(self.driver)

