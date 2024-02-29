from selenium.webdriver.common.by import By


class search_employeeClass:
    Click_Customers_button_Xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    Click_Customer_Xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    Text_Email_Xpath = "//input[@id='SearchEmail']"
    Click_Search_button_Xpath = "//button[@id='search-customers']"
    Click_Check_box_Xpath = "//input[@name='checkbox_customers']"
    Click_Edit_button_Xpath = "//a[@class='btn btn-default']"
    Text_password1_Xpath = "//input[@id='Password']"
    Click_Change_password_Xpath = "//button[@name='changepassword']"
    Click_Save_Button_Xpath = "//button[@name='save']"
    Success_message_Xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver

    def Customers_Button(self):
        self.driver.find_element(By.XPATH, self.Click_Customers_button_Xpath).click()

    def Customer(self):
        self.driver.find_element(By.XPATH, self.Click_Customer_Xpath).click()

    def Email(self, email):
        self.driver.find_element(By.XPATH, self.Text_Email_Xpath).send_keys(email)

    def Search(self):

        self.driver.find_element(By.XPATH, self.Click_Search_button_Xpath).click()

    def CheckBox(self):

        self.driver.find_element(By.XPATH, self.Click_Check_box_Xpath).click()

    def Edit(self):

        self.driver.find_element(By.XPATH, self.Click_Edit_button_Xpath).click()

    def password_edit(self, change):
        self.driver.find_element(By.XPATH, self.Text_password1_Xpath).send_keys(change)

    def password_Change(self):
        self.driver.find_element(By.XPATH, self.Click_Change_password_Xpath).click()

    def Click_save_Button(self):
        self.driver.find_element(By.XPATH, self.Click_Save_Button_Xpath).click()

    def validate_Success_message(self):
        try:
            self.driver.find_element(By.XPATH, self.Success_message_Xpath)
            return "pass"
        except:
            return "fail"
