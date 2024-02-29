#1/2/2024
import time

import pytest
from selenium import webdriver
# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     driver.get('https://admin-demo.nopcommerce.com/login')
#     driver.maximize_window()
#     return driver

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# @pytest.fixture
# def setup():
#
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     driver.get("https://admin-demo.nopcommerce.com/login")
#     return driver


##multiple browser invocation at runtime
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

def pytest_addoption(parser):
    parser.addoption("--browser")# browser can recongrise the pytest/python
@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        print("Test browser chrome")
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        print("Test browser firefox")
        driver = webdriver.Firefox()

    elif browser == 'edge':
        print("Test browser is Edge")
        driver = webdriver.Edge()

    else:
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(params=[
    ("admin@yourstore.com", "admin", "Pass"),
    ("admin@yourstore.com1", "admin", "Fail"),
    ("admin@yourstore.com1", "admin1", "Fail"),
    ("admin@yoursstore.com", "admin1", "Fail")
])
def DataForLogin(request):
    return request.param