import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Page_loginClass:
    Text_username_Xpath = "//input[@id='Email']"
    Text_password_Xpath = "//input[@id='Password']"
    Click_Login_Button_Xpath = "//button[@type='submit']"
    Click_logout_button_Xpath = "//a[normalize-space()='Logout']"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def username(self,useremail):
        self.driver.find_element(By.XPATH, self.Text_username_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Text_username_Xpath).send_keys(useremail)

    def password(self, password):
        self.driver.find_element(By.XPATH, self.Text_password_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Text_password_Xpath).send_keys(password)

    def login_button(self):
        self.driver.find_element(By.XPATH, self.Click_Login_Button_Xpath).click()

    def logout_button(self):

        try:
            self.wait.until(
                expected_conditions.presence_of_element_located(By.XPATH, self.Click_logout_button_Xpath))
            self.driver.find_element(By.XPATH, self.Click_logout_button_Xpath).click()
        except:
            pass

    def Vrifylogin(self):
        try:
            self.driver.find_element(By.XPATH,self.Click_logout_button_Xpath)
            self.driver.find_element(By.XPATH, self.Click_logout_button_Xpath).click()
            return "pass"
        except:
            return "fail"
