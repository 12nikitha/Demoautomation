import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #WEBDRIVER_MANGER are used to set path directly ,instead we seariching chrome and finding path
from selenium.webdriver.chrome.service import Service #Service Object: Using Service() to properly pass the executable path for the Chrome driver to webdriver.Chrome().
from POMDemo.Pages.Testlogin import Login
from POMDemo.Pages.HomePage import Homepage
import HtmlTestRunner
service = Service(ChromeDriverManager().install())
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(2)


    def testlogin(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        signup= Login(self.driver)
        time.sleep(1)

        signup.enter_username("Admin")
        signup.enter_password("admin123")
        time.sleep(2)
        signup.click_login()
        time.sleep(2)
        homepage = Homepage(driver)
        # time.sleep(2)
        homepage.enter_welcome()
        time.sleep(2)
        homepage.enter_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/nikitha/learn_python/selenium1/Automation1/POMDemo/Report"))






