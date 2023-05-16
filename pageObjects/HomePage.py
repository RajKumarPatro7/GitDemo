from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    shop_linkText = (By.LINK_TEXT, "Shop")
    name_field_CSS = (By.CSS_SELECTOR, "input[name = 'name']")
    email_field_CSS = (By.CSS_SELECTOR, "input[name = 'email']")
    pass_field_CSS = (By.CSS_SELECTOR, "#exampleInputPassword1")
    gender_field_CSS = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    employee_status_CSS = (By.CSS_SELECTOR, "label[for = 'inlineRadio1']")
    submit_button_CSS = (By.CSS_SELECTOR, "input[class= 'btn btn-success']")
    success_msg_CSS = (By.CSS_SELECTOR, "div[class= 'alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop_linkText).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def name_field(self):
        return self.driver.find_element(*HomePage.name_field_CSS)

    def email_field(self):
        return self.driver.find_element(*HomePage.email_field_CSS)

    def pass_field(self):
        return self.driver.find_element(*HomePage.pass_field_CSS)

    def gender_select(self):
        return self.driver.find_element(*HomePage.gender_field_CSS)

    def select_employee_status(self):
        return self.driver.find_element(*HomePage.employee_status_CSS)

    def click_submit(self):
        return self.driver.find_element(*HomePage.submit_button_CSS)

    def success_message(self):
        return self.driver.find_element(*HomePage.success_msg_CSS)



