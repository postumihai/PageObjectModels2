import pytest
from selenium import webdriver
from src.pages.homepage import Homepage
from src.pages.sign_in_page import SignInPage


@pytest.mark.usefixtures("setup")
class TestOne:

    def test_1(self, setup):

        homepage = Homepage(self.driver)
        sign_in_page = SignInPage(self.driver)
        homepage.click_sign_in()
        sign_in_page.select_username()
        sign_in_page.select_password()
        sign_in_page.click_login()
        homepage.get_username()
