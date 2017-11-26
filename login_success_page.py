# conding: UTF-8

class login_success_page():
    def __init__(self,driver):
        self.driver = driver


    def get_text(self,by,value):
        element = self.driver.find_element(by=by,value=value)
        return element.text
