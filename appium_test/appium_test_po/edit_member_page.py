# -*- coding: utf-8 -*-
#添加编辑成员界面，编辑完成后，保存，再返回选择手东添加成员界面
from appium.webdriver.common.mobileby import MobileBy

from appium_test.appium_test_po.basepage import BasePage


class EditMemberPage(BasePage):
    #接受上个页面的driver 每个页面都需要
    # def __init__(self,driver):
    #     self.driver = driver
    def edit_member(self,name,gender,mail):
        # self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("zhangsan")
        # self.driver.find_element_by_xpath("//*[@resource-id="
        #                                   "'com.tencent.wework:id/b81'and @text='男']").click()
        # self.driver.find_element_by_xpath("//*[@text='男']").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'邮箱')]"
        #                                   "/../android.widget.EditText").send_keys("zhangsan@qq.com")
        # self.driver.find_element_by_id("com.tencent.wework:id/ie7").click()
        name_ele = (MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText")
        self.find(name_ele).send_keys(name)
        # gender = '女'
        #查找元素并点击元素
        self.find_and_click((MobileBy.XPATH,"//*[@text='男']"))
        if gender == "女":
            self.find_and_click((MobileBy.XPATH,"//*[@text='女']"))
        else:
            self.find_and_click((MobileBy.XPATH,"//*[@text='男']"))

        self.find((MobileBy.XPATH,"//*[contains(@text,'邮箱')]/../android.widget.EditText")).send_keys(mail)
        self.find_and_click((MobileBy.ID,"com.tencent.wework:id/ie7"))
        from appium_test.appium_test_po.add_member_page import AddMembrePage
        return AddMembrePage(self.driver)
