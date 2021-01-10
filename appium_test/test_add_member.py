# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
def test_demo():
    caps = {}
    caps["platformName"] = "Android"
    #方便辨识app，可以不填写
    caps["deviceName"] = "wework"
    caps["appPackage"] = "com.tencent.wework"
    caps["appActivity"] = ".launch.LaunchSplashActivity"
    # 不清空缓存启动app
    caps["noReset"] = "true"
    # 设置等待页面空闲状态的时间为0s
    caps['settings[waitForIdleTimeout]'] = 0
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    caps['ontStopAppOnRest'] = 'true'
    # 显式等待10s
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[@text='通讯录']").click()
    driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector().'
                             'scrollable(true).instance(0)).'
                             'scrollIntoView(new UiSelector().'
                             'text("添加成员").instance(0));').click()
    driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
    driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("zhangsan6")
    driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/b81'and @text='男']").click()
    driver.find_element_by_xpath("//*[@text='男']").click()
    driver.find_element_by_xpath("//*[contains(@text,'邮箱')]/../android.widget.EditText").send_keys("zhangsan6@qq.com")
    driver.find_element_by_id("com.tencent.wework:id/ie7").click()
    # ele = driver.find_element_by_xpath("//*[@text='添加成功']").text
    #获取toast信息
    ele = driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
    assert ele == '添加成功'









