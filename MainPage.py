#conding:UTF-8

class MainPage():

    def __init__(self,driver):
        self.driver = driver

    def go_to_login(self):
        element = self.driver.find_element_by_id('titleSave')
        element.click()




