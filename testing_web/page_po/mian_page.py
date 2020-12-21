# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


from testing_web.page_po.basepage import BasePage
from testing_web.page_po.contact_page import ContactPage
#首页
class MainPage(BasePage):
    _base_url ='https://work.weixin.qq.com/wework_admin/frame#index'
    def goto_contact_page(self):

        self.find(By.ID,"menu_contacts").click()
        #到通讯录页面
        return ContactPage(self.driver)
    def goto_add_member(self):
        from testing_web.page_po.add_member_page import AddMemberPage
        self.find(By.ID,"menu_index").click()
        while True:
            self.find(By.CSS_SELECTOR,"#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt."
                                      "js_service_list > a:nth-child(1) > div > span.ww_indexImg.ww_indexImg_AddMember").click()
            element_1=self.finds(By.ID,"username")
            if len(element_1)>0:
                break
        return AddMemberPage(self.driver)

