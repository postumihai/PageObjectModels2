import time

from selenium.webdriver import Keys
from seleniumpagefactory.Pagefactory import PageFactory


class SignInPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'user_name': ('ID', "react-select-2-input"),
        'password': ('ID', "react-select-3-input"),
        'login_btn': ('ID', "login-btn")
    }

    def select_username(self):
        self.user_name.set_text('demouser\n')
        time.sleep(2)

    def select_password(self):
        self.password.set_text('testingisfun99\n')

        time.sleep(2)

    def click_login(self):
        self.login_btn.click()
