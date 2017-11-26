# coding: UTF-8
from appium import webdriver
import time
import unittest

from LoginPage import LoginPage
from MainPage import MainPage
from login_success_page import login_success_page


class Login(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0.1"
        desired_caps["appPackage"] = "com.sina.weibo"
        desired_caps["appActivity"] = "com.sina.weibo.SplashActivity"
        desired_caps["deviceName"] = "f7436a7f"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(5)

    def test02(self):
        MainPage(self.driver).go_to_login()
        time.sleep(3)
        LoginPage(self.driver).login1()
        time.sleep(5)
        self.assertEqual(login_success_page(self.driver).get_text('id','tvNick'),u'可爱de小胖妞')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

