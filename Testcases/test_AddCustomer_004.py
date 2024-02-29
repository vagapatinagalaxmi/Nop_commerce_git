import random
import string

import allure
import pytest
from allure_commons.types import AttachmentType

from PageObject.CostomerPage import Add_CustomerClass
from Utilities.Logger import log_generator
from PageObject.Loginpage import Page_loginClass
from Utilities.readconfigfile import Readconfig


@pytest.mark.usefixtures
class Test_AddCustomer:
    UserEmail = Readconfig.getEmail()
    password = Readconfig.getPassword()
    log = log_generator()


    def test_Add_Customer_005(self, setup):
        self.log.info("Test case Test_Add_Customer started")
        self.log.info("browser navigated to nopcommerce.com")
        self.driver = setup
        self.lp = Page_loginClass(self.driver)
        self.log.info("Enter the UserEmail")
        self.lp.username(self.UserEmail)
        self.log.info("Enter the password")
        self.lp.password(self.password)
        self.log.info("Click to Login Button")
        self.lp.login_button()
        self.ac = Add_CustomerClass(self.driver)
        self.log.info("Click to Customer menu button")
        self.ac.Click_Customer_Button()
        self.log.info("Click the Customer sub button ")
        self.ac.click_Customer_button()
        self.log.info("Click Add customer Button")
        self.ac.Add_new_employee()
        self.log.info("Generating Random email")
        email = Generate_email()
        self.log.info("Generating email--->" + str(email))
        self.ac.Enter_email(email)
        self.log.info("Entering Password")
        self.ac.Enter_password("Credence@101")
        self.log.info("Selecting Gender")
        self.ac.Click_Gender("male")
        self.log.info("Enter date of birth")
        self.ac.Enter_Dob("12/02/2023")
        self.log.info("Enter company name")
        self.ac.Enter_Company_name("Credence")
        self.log.info("Click the Check box")
        self.ac.Click_is_tax_exempt()
        self.log.info("Entering Newsletter")
        self.ac.Enter_Newsletter()
        self.log.info("Select Newsletter list")
        self.ac.Click_NewsLetter_list()
        self.log.info("Entering Manager of vendor")
        self.ac.Enter_Manager_of_Vender("Vendor 1")
        self.log.info("Click the Active checkbox")
        self.ac.Click_Activ()
        self.log.info("Enter the Admin comments")
        self.ac.Enter_Admin_Comments("Automation testing")
        self.log.info("Click save button")
        self.ac.Click_save_Button()
        if self.ac.Validate_Success_Message() == "pass":
            self.log.info("Test case test_Add_Customer passed")
            self.log.info("take the screenshots")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_AddCustomer -pass.png",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshot\\test_addCustomer_003_pass.png")
            self.lp.logout_button()
            assert True
        else:
            self.log.info("Test case test_Add_customer failed")
            self.log.info("Take the screenshots")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_AddCustomer_fail.png",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshot\\test_addCustomer_003_fail.png")
            assert False


def Generate_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=4))
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])
    return f" {username}@{domain}"
