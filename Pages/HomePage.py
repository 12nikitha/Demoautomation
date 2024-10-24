import time

from selenium.webdriver.common.by import By
from POMDemo.locators.Locators import Locator

class Homepage:
    def __init__(self,driver):
        self.driver=driver
        self. welcome_button = Locator.welcome_button
        self.logout_button = Locator.logout_button
    def enter_welcome(self):

        self.driver.find_element(By.CLASS_NAME, Locator.welcome_button).click()
    def enter_logout(self):
        self.driver.find_element(By.CLASS_NAME, Locator.welcome_button).click()




