import time

import allure
import pytest
from allure_commons.types import AttachmentType

from PageObject.CostomerPage import Add_CustomerClass
from PageObject.Loginpage import Page_loginClass
from Utilities import XLUtils
from Utilities.Logger import log_generator
from Utilities.readconfigfile import Readconfig


class Test_AddCustomer_DDT:
    UserEmail = Readconfig.getEmail()
    password = Readconfig.getPassword()
    Excel_File_Path = "C:\\Fremework projects\\nopcommerce\\nopcommerce_framework\\Testcases\\Testdata\\New Microsoft Excel Worksheet.xlsx"
    log = log_generator()


    def test_AddCustomer_DDT_006(self, setup):
        self.log.info("Test case test_AddCustomer_DDt_004 started")
        self.log.info("Browser navigated to nopcommerce.com")
        self.driver = setup

        self.lp = Page_loginClass(self.driver)
        self.log.info("Entering UserEmail-->" + self.UserEmail)
        self.lp.username(self.UserEmail)
        self.log.info("Entering password-->" + self.password)
        self.lp.password(self.password)
        self.log.info("Click the login Button")
        self.lp.login_button()
        self.ac = Add_CustomerClass(self.driver)
        self.log.info("Click the Customer main button")
        self.ac.Click_Customer_Button()
        self.log.info("Click customer sub button")
        self.ac.click_Customer_button()
        self.log.info("Click the AddCustomer button")
        self.ac.Add_new_employee()
        self.rows = XLUtils.numRows(self.Excel_File_Path, 'Sheet1')
        status_list = []
        for r in range(2, self.rows + 1):
            self.email = XLUtils.readData(self.Excel_File_Path, 'Sheet1', r, 2)
            self.password = XLUtils.readData(self.Excel_File_Path, 'Sheet1', r, 3)
            self.Company_name= XLUtils.readData(self.Excel_File_Path, 'Sheet1', r, 4)
            print("iterated variable i-->" + str(r))
            print("email--->" + self.email)
            print("password-->" + self.password)
            print("company_name" + self.Company_name)
            self.ac.Enter_email(self.email)
            self.ac.Enter_password(self.password)
            self.ac.Enter_Company_name(self.Company_name)
            self.ac.Click_save_Button()
            if self.ac.Validate_Success_Message() == "pass":
                status_list.append("pass")
                XLUtils.writeData(self.Excel_File_Path, 'Sheet1', r, 5, "Pass")
                self.log.info("Take the screenshot")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_AddCustomer_004-pass.png",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshot\\test_addCustomer_DDT_004_pass.png")
                self.log.info("Click Add_new Button")
                self.ac.Add_new_employee()
            else:
                status_list.append("repeated")
                XLUtils.writeData(self.Excel_File_Path, 'Sheet1', r, 5, "fail")
                self.log.info("Take the screenshot")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_AddCustomer-fail.png",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshot\\test_addCustomer_DDT_004_fail.png")

        print(status_list)
        time.sleep(5)
        self.lp.logout_button()
        if "pass" in status_list:
            self.log.info("test_addCustomer_ddt_004 is Passed")
            assert True
        elif "repeated" in status_list:
            self.log.info("Email already Registered")
            self.log.info("test_addCustomer_ddt_004 is Passed")
            assert True
        else:
            self.log.info("test_addCustomer_ddt_004 is Failed")
            assert False
        self.log.info("test_addCustomer_ddt_004 is Completed")
