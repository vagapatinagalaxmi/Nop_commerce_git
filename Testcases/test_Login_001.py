## 1/2/2024
import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Utilities.Logger import log_generator
from PageObject.Loginpage import Page_loginClass
from Utilities.readconfigfile import Readconfig


@pytest.mark.usefixtures("setup")
class Test_UserLogin:
    UserEmail = Readconfig.getEmail()
    password = Readconfig.getPassword()
    log = log_generator()

    @pytest.mark.sanity
    @allure.feature("page titel")
    @allure.title("Non-com Test Page title")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link("https://admin-demo.nopcommerce.com/login")
    @allure.story("verify the page")
    @allure.issue("ABC_!@#")
    @allure.description("Test description")
    def test_verify_001(self, setup):
        self.log.info("Test case test_verify started")
        self.driver = setup
        self.log.info("browser opening navigating to nop.com")
        self.log.info("page title-->" + self.driver.title)
        print(self.driver.title)
        if self.driver.title == "Your store. Login":
            self.log.info("Test case  test_verify passed")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_verify-pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshot\\test_verify_pass.png")
            print("Test Case Passed")
            assert True
        else:
            self.log.info("Test case test_verify failed")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_verify-fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshot\\test_verify_fail.png")
            print("Test Case Failed")
            assert False

    @pytest.mark.sanity
    def test_Login_002(self, setup):
        self.log.info("Test case test_Login started")
        self.log.info("browser opene navigated to nop.com")
        self.driver = setup
        self.lp = Page_loginClass(self.driver)
        self.log.info("Entering UserEmail")
        self.lp.username(self.UserEmail)
        self.log.info("Entering username--->" + self.UserEmail)
        self.log.info("entering password")
        self.lp.password(self.password)
        self.log.info("password-->" + self.password)
        self.log.info("Click button")
        self.lp.login_button()
        self.lp.logout_button()

        if self.lp.Vrifylogin() == "pass":
            self.log.info("Test case test_Login passed")
            self.log.info("Take the Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Login-pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(
                "C:\\Fremework projects\\nopcommerce\\nopcommerce_framework\\Screenshot\\test_Login_pass.png")
            self.log.info('clickLogout button')

            assert True
        else:
            self.log.info("test case test_Login failed")
            self.log.info("Take the Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Login-fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(
                "C:\\Fremework projects\\nopcommerce\\nopcommerce_framework\\Screenshot\\test_Login_fail.png")
            assert False
        self.log.info("test case test_Login completed")
