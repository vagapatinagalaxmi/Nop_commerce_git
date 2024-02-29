import allure
from allure_commons.types import AttachmentType

from PageObject.Loginpage import Page_loginClass
import pytest

from Utilities.Logger import  log_generator


@pytest.mark.usefixtures("DataForLogin")
class Test_LoginParams:
    log = log_generator()

    @pytest.mark.sanity
    def test_Login_params_004(self, setup, DataForLogin):
        self.log.info("Test case test_Login_Param_004 started")
        self.driver = setup
        self.log.info("Browser is opened")
        self.lp = Page_loginClass(self.driver)
        self.log.info("Entering_username")
        self.lp.username(DataForLogin[0])
        print("\n"+DataForLogin[0])
        self.log.info("Entering_Password" + DataForLogin[0])
        self.lp.password(DataForLogin[1])
        print(DataForLogin[1])
        self.log.info("Click on login_button" + DataForLogin[1])
        self.lp.login_button()
        statues_of_login_list = []
        if self.lp.Vrifylogin() == "pass":
            self.log.info("Test case passed")
            if DataForLogin[2] == "Pass":
                self.log.info("Expected pass")
                statues_of_login_list.append("pass")
                self.log.info("Taking screen short")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_004-Pass",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshot\\test_-004_pass.png")
                self.log.info("Click on logout button")
                self.lp.logout_button()
            elif DataForLogin[2] == "Fail":
                self.log.info("Expected test case failed")

                statues_of_login_list.append("fail")
                self.log.info("Taking screen short")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Login-Params_04_fail",
                              attachment_type=AttachmentType.PNG)
                self.log.info("Click on logout button")
                self.lp.logout_button()

        elif self.lp.Vrifylogin() == "fail":
            self.log.info(" Test case  failed")
            if DataForLogin[2] == "Fail":
                self.log.info("Expected result failed")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Login_params_04-pass",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshot\\test_Login_pass.png")
                statues_of_login_list.append("pass")
            elif DataForLogin[2] == "Pass":
                self.log.info("Expected result Failed")
                statues_of_login_list.append("fail")
                self.log.critical("Taking screen short")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Login_Params_04_fail",
                          attachment_type=AttachmentType.PNG)

        print(statues_of_login_list)
        if "pass" in statues_of_login_list:
            self.log.info("Test case test_Login_Param_004 passed")
            assert True
        else:
            self.log.info(" Test case test_Loin_Params_oo4 failed")
            assert False
        self.log.info("Test case test_User_Login_Params_004 completed")
