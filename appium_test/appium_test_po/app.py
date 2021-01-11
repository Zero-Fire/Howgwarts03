# -*- coding: utf-8 -*-
#启动app，关闭app，重启app，进入首页等
from appium import webdriver

from appium_test.appium_test_po.basepage import BasePage
from appium_test.appium_test_po.main_page import MainPage
class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            # 方便辨识app，可以不填写
            caps["deviceName"] = "wework"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            # 不清空缓存启动app
            caps["noReset"] = "true"
            # 设置等待页面空闲状态的时间为0s
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            caps['ontStopAppOnRest'] = 'true'
            # 显式等待10s
            self.driver.implicitly_wait(10)
        else:
            # 拿到设置的参数 直接启动 app，更具caps内设置的信息，启动app
            self.driver.launch_app()
        return self
    def stop(self):
        self.driver.quit()
    def restart(self):
        self.driver.close()
        self.driver.launch_app()
        #返回一个类对象
    def goto_main(self)->MainPage:
        return MainPage(self.driver)