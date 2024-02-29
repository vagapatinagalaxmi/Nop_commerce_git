import time

import allure
import pytest
import openpyxl
from allure_commons.types import AttachmentType

from PageObject.Loginpage import Page_loginClass
from Utilities import XLUtils
from Utilities.Logger import log_generator


# from Utilities.readconfigfile import Readconfig


class Test_login_DDt:
    log = log_generator()
    Excel_File_Path = "C:\\Fremework projects\\nopcommerce\\nopcommerce_framework\\Testcases\\Testdata\\logindata.xlsx"

    def test_login_ddt_003(self, setup):
        self.log.info("Test case test_login_ddt started")
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.log.info("browser open navigated to nop.com")
        self.lp = Page_loginClass(self.driver)
        self.rows = XLUtils.numRows(self.Excel_File_Path, 'Logindata')
        print("number of rows--->", self.rows)
        statues_of_login_list = []
        self.log.info("Creating for loop")
        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.Excel_File_Path, 'Logindata', r, 2)
            self.password = XLUtils.readData(self.Excel_File_Path, 'Logindata', r, 3)
            self.Expected_Login_Result = XLUtils.readData(self.Excel_File_Path, 'Logindata', r, 4)
            #print("iteration variable-->" + str(r))
            # print("username--> " + self.username)
            # print("password-->" + self.password)
            # print("Expected_Login_Result-->" + self.Expected_Login_Result)
            self.log.info("Entering username")
            self.lp.username(self.username)
            print("username-->" + self.username)
            self.log.info("Entering password")
            self.lp.password(self.password)
            print("password-->" + self.password)
            self.log.info("Click login button")
            self.lp.login_button()
            self.log.info("Click logout button")
            self.lp.logout_button()
            # self.log.info("Verify the login")

            if self.lp.Vrifylogin() == "pass":
                self.log.info("Login pass")
                XLUtils.writeData(self.Excel_File_Path, 'Logindata', r, 5, "Pass")
                if self.Expected_Login_Result == 'pass':
                    self.log.info("Expected pass")
                    statues_of_login_list.append("pass")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_Login-pass.png",
                                  attachment_type=AttachmentType.PNG)
                    self.log.info("Take Screenshot")
                    self.driver.save_screenshot("..\\Screenshot\\test_Login_pass.png")
                    self.log.info("Click logout button")
                    self.lp.logout_button()

                elif self.Expected_Login_Result == "fail":
                    self.log.info("Expected Fail")
                    statues_of_login_list.append("fail")
                    self.log.info("Take Screenshot")
                    self.driver.save_screenshot("..\\Screenshot\\test_Login_fail.png")
                    XLUtils.writeData(self.Excel_File_Path, 'Logindata', r, 5, "Pass")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_Login-fail.png",
                                  attachment_type=AttachmentType.PNG)

                    self.log.info("Click Logout Button")
                    self.lp.logout_button()
            elif self.lp.Vrifylogin() == 'fail':
                self.log.info(" login Fail")
                XLUtils.writeData(self.Excel_File_Path, 'Logindata', r, 5, "Fail")
                if self.Expected_Login_Result == "fail":
                    self.log.info("Expected Login fail")
                    statues_of_login_list.append("pass")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_Login-pass.png",
                                  attachment_type=AttachmentType.PNG)
                    self.driver.save_screenshot("..\\Screenshot\\test_Login_pass.png")
                elif self.Expected_Login_Result == "pass":
                    self.log.info("Expected pass")
                    statues_of_login_list.append("fail")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_Login-fail.png",
                                  attachment_type=AttachmentType.PNG)
                    self.driver.save_screenshot("..\\Screenshot\\test_Login_fail.png")
        print("statues_of_list" + str(statues_of_login_list))
        if "fail" in statues_of_login_list:

            self.log.info("Test_case test_user_login_DDT_005 is Failed")
            assert False
        else:

            self.log.info("Test_case test_user_login_DDT_005 is Passed ")
            assert True
        self.log.info("Test_case test_login_DDT is Completed")
