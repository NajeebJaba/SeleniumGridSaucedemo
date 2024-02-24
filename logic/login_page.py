from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_field = "user-name"
        self.password_field = "password"
        self.login_button = "login-button"

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element_by_id(self.username_field).send_keys(username)
        self.driver.find_element_by_id(self.password_field).send_keys(password)
        self.driver.find_element_by_id(self.login_button).click()