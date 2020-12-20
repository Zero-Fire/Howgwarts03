# -*- coding: utf-8 -*-
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address="127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    data = driver.get_cookies()
    with open ("data_cookie.yaml","w",encoding="utf-8") as f:
        yaml.dump(data,f)

def test_login():
    opt = webdriver.ChromeOptions()
    opt.debugger_address= "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()
    ele = (By.CSS_SELECTOR,".ww_operationBar .js_add_member")
    WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable(ele))
    while True:
        driver.find_element(*ele).click()
        element = driver.find_elements_by_id('username')
        if len(element)>0:
            break
    driver.find_element_by_id('username').send_keys("张三")
    driver.find_element_by_id("memberAdd_acctid").send_keys("zhangsan")
    driver.find_element_by_id('memberAdd_mail').send_keys("zhangsan@qq.com")
    driver.find_element_by_css_selector('.js_btn_save').click()
    sleep(3)
    eles = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
    name_list = []
    for value in eles:
        print(value.get_attribute("title"))
        name_list.append(value.get_attribute("title"))
    assert "张三" in name_list










