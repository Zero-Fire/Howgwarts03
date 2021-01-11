# -*- coding: utf-8 -*-
#添加成员界面，点击手动输入成员进入添加编辑成员界面
from appium_test.appium_test_po.basepage import BasePage
from appium_test.appium_test_po.edit_member_page import EditMemberPage
class AddMembrePage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    def click_add_member(self):
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        return EditMemberPage(self.driver)
    #断言是否添加成功
    def estimate(self):
        #获取toast信息
        mytoast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        return mytoast
