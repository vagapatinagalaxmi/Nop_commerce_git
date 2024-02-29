from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_CustomerClass:
    Click_Customers_button_Xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    Click_Customer_Xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    Click_Add_new_Xpath = "//a[normalize-space()='Add new']"
    Text_Enter_Email_Xpath = "//input[@id='Email']"
    Text_Enter_Password_Xpath = "//input[@id='Password']"
    Text_Enter_Firstname_Xpath = "//input[@id='FirstName']"
    Text_Enter_Lastname_Xpath = "//input[@id='LastName']"
    Radio_Button_Gender_Male_Xpath = "//input[@id='Gender_Male']"
    Radio_Button_Gender_Female_Xpath = "//input[@id='Gender_Female']"
    Text_Enter_Dob_Xpath = "//input[@id='DateOfBirth']"
    Text_Company_name_Xpath = "//input[@id='Company']"
    Click_Is_tax_exempt_Xpath = "//input[@id='IsTaxExempt']"
    Text_Newsletter_Xpath = "/html/body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]"
    Click_Newsletter_list_Xpath = "//li[normalize-space()='Test store 2']"
    Text_Manager_of_vendor_Xpath = "//select[@id='VendorId']"
    Click_Active_Xpath = "//input[@id='Active']"
    Text_Admin_comments_Xpath = "//textarea[@id='AdminComment']"
    Click_Save_Button_Xpath = "//button[@name='save']"
    Success_Message1_Xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):

        self.driver = driver

    def Click_Customer_Button(self):
        self.driver.find_element(By.XPATH, self.Click_Customers_button_Xpath).click()

    def click_Customer_button(self):
        self.driver.find_element(By.XPATH, self.Click_Customer_Xpath).click()

    def Add_new_employee(self):

        self.driver.find_element(By.XPATH, self.Click_Add_new_Xpath).click()

    def Enter_email(self, email):
        self.driver.find_element(By.XPATH,self.Text_Enter_Email_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Text_Enter_Email_Xpath).send_keys(email)

    def Enter_password(self, password):
        self.driver.find_element(By.XPATH, self.Text_Enter_Password_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Text_Enter_Password_Xpath).send_keys(password)

    def Enter_Firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.Text_Enter_Firstname_Xpath).send_keys(firstname)

    def Enter_Lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.Text_Enter_Lastname_Xpath).send_keys(lastname)

    def Click_Gender(self, gender):
        if gender == 'male':

            self.driver.find_element(By.XPATH, self.Radio_Button_Gender_Male_Xpath).click()
        elif gender == 'female':
            self.driver.find_element(By.XPATH, self.Radio_Button_Gender_Female_Xpath).click()

    def Enter_Dob(self, date):
        self.driver.find_element(By.XPATH, self.Text_Enter_Dob_Xpath).send_keys(date)

    def Enter_Company_name(self, company_name):
        self.driver.find_element(By.XPATH, self.Text_Company_name_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Text_Company_name_Xpath).send_keys(company_name)

    def Click_is_tax_exempt(self):
        self.driver.find_element(By.XPATH, self.Click_Is_tax_exempt_Xpath).click()

    def Enter_Newsletter(self):
        self.driver.find_element(By.XPATH, self.Text_Newsletter_Xpath).click()

    def Click_NewsLetter_list(self):
        self.driver.find_element(By.XPATH, self.Click_Newsletter_list_Xpath).click()

    def Enter_Manager_of_Vender(self, value):
        Select(self.driver.find_element(By.XPATH, self.Text_Manager_of_vendor_Xpath)).select_by_visible_text(value)

    def Click_Activ(self):
        self.driver.find_element(By.XPATH, self.Click_Active_Xpath).click()

    def Enter_Admin_Comments(self, comment):
        self.driver.find_element(By.XPATH, self.Text_Admin_comments_Xpath).send_keys(comment)

    def Click_save_Button(self):
        self.driver.find_element(By.XPATH, self.Click_Save_Button_Xpath).click()

    def Validate_Success_Message(self):
        try:
            self.driver.find_element(By.XPATH, self.Success_Message1_Xpath)
            return "pass"
        except:
            return "fail"
