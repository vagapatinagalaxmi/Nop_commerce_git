import random
import string
import time

import allure
import pytest
from allure_commons.types import AttachmentType

from PageObject.Loginpage import Page_loginClass
from Utilities.Logger import log_generator
from Utilities.readconfigfile import Readconfig
from PageObject.SearchPage import search_employeeClass


class Test_search_edit:
    UserEmail = Readconfig.getEmail()
    password = Readconfig.getPassword()
    log = log_generator()


    def test_search_edit_007(self, setup):
        self.log.info("Test case test_search_edit_006 started")
        self.log.info("Browser invoked to nop.com")
        self.driver = setup
        self.lp = Page_loginClass(self.driver)
        self.log.info("Entering username")
        self.lp.username(self.UserEmail)
        self.log.info("Enter password")
        self.lp.password(self.password)
        self.log.info("Click login button")
        self.lp.login_button()
        self.sp = search_employeeClass(self.driver)
        self.log.info("Click Customer main button")
        self.sp.Customers_Button()
        self.sp.Customer()
        self.log.info("Enter email")
        self.sp.Email("asd@gmail.com")
        self.log.info("Click search button")
        self.sp.Search()
        time.sleep(0.5)
        self.log.info("select checkbox")
        self.sp.CheckBox()
        self.log.info("Click Edit button")
        self.sp.Edit()
        self.log.info("Enter password")
        password=Generate_password()
        self.sp.password_edit(password)
        self.log.info("Click password change")
        self.sp.password_Change()
        self.log.info("Click save Button")
        self.sp.Click_save_Button()
        if self.sp.validate_Success_message() == "pass":
            self.log.info("Test case test_search_edit_006 passed")
            self.driver.save_screenshot("C:\\Fremework projects\\nopcommerce\\nopcommerce_framework\\Screenshot\\test_search_edit_007_pass.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_search_edit_007_pass.png",
                          attachment_type=AttachmentType.PNG)
            self.lp.logout_button()
            assert True
        else:
            self.log.info("Test case test_search_edit_007 failed")
            self.log.info("Take a screenshot")
            self.driver.save_screenshot("C:\\Fremework projects\\nopcommerce\\nopcommerce_framework\\Screenshot\\test_search_edit_007_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_search_edit_007_pass.fail",
                          attachment_type=AttachmentType.PNG)
            assert False
        self.log.info("Test case test_search_edit_006 completed")
# def Generate_email():
#     username = ''.join(random.choices(string.ascii_lowercase, k=4))
#     domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])
#     return f" {username}@{domain}"
def Generate_password():
    password=(random.choices(string.ascii_letters,k=4))
    return password