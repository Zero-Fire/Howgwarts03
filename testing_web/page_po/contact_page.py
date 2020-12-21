# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
#通讯录页面
from testing_web.page_po.basepage import BasePage


class ContactPage(BasePage):
    def click_add_member(self):
        from testing_web.page_po.add_member_page import AddMemberPage
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        self.wait_for_click(ele)
        while True:
            self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            element = self.finds(By.ID,'username')
            if len(element) > 0:
                break
        #到添加成员页面
        return AddMemberPage(self.driver)
    #通讯录页面断言
    def get_member(self):
        time.sleep(2)
        eles = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for value in eles:
            name_list.append(value.get_attribute("title"))
        return name_list
