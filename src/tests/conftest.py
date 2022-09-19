import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        service_obj = Service("C:/Users/ecm/PycharmProjects/PageObjectModels2/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == 'firefox':
        service_obj = Service("C:/Users/ecm/PycharmProjects/PageObjectModels2/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://bstackdemo.com/")
    request.cls.driver = driver
    yield
    driver.close()
