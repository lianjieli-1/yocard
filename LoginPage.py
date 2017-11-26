#conding:UTF-8

class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.username = self.driver.find_element_by_id("etLoginUsername")
        self.pwd = self.driver.find_element_by_id("etPwd")
        self.login = self.driver.find_element_by_id("rlLogin")


    def login1(self):
        self.username.send_keys("673505529@qq.com")
        self.pwd.send_keys("L890316")
        self.login.click()