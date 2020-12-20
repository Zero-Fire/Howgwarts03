# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#通讯录页面
class ContactPage:
    def click_add_member(self):
        from testing_web.page_po.add_member_page import AddMemberPage
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(ele))
        while True:
            driver.find_element(*ele).click()
            element = driver.find_elements_by_id('username')
            if len(element) > 0:
                break
        #到添加成员页面
        return AddMemberPage()
    #通讯录页面断言
    def get_member(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        time.sleep(2)
        eles = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for value in eles:
            name_list.append(value.get_attribute("title"))
        return name_list
