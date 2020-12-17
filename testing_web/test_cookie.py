# -*- coding: utf-8 -*-
from time import sleep

import yaml
from selenium import webdriver

def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address="127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    data = driver.get_cookies()
    with open ("data_cookie.yaml","w",encoding="utf-8") as f:
        yaml.dump(data,f)
def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open ("data_cookie.yaml",encoding="utf-8") as f:
        cookies = yaml.safe_load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_css_selector("#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(1) > div > span.ww_indexImg.ww_indexImg_AddMember").click()
    driver.find_element_by_css_selector("#username").send_keys("张三")
    driver.find_element_by_css_selector("#memberAdd_acctid").send_keys("1111")
    driver.find_element_by_css_selector("#memberAdd_phone").send_keys("12345678901")
    driver.find_element_by_link_text("保存").click()
    sleep(3)
    driver.quit()
