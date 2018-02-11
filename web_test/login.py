
def login(self):
    driver = self.driver
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin123")
    driver.find_element_by_xpath("/html/body/div/div/form/button").click()