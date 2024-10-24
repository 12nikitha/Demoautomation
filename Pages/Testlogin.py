from selenium.webdriver.common.by import By

from POMDemo.locators.Locators import Locator
class Login():
    def __init__(self,driver):
        self.driver = driver
        self.username_textbox = Locator.username_textbox
        self.password_textbox = Locator.password_textbox
        self.login_button = Locator. login_button
    def enter_username(self,name):
        self.driver.find_element(By.NAME, Locator.username_textbox).clear()
        self.driver.find_element(By.NAME, Locator.username_textbox).send_keys(name)

    def enter_password(self,code):
        self.driver.find_element(By.NAME, Locator.password_textbox).clear()
        self.driver.find_element(By.NAME, Locator.password_textbox).send_keys(code)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()



