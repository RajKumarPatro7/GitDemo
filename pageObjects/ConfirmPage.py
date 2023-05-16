from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:
    Success_checkout_button = (By.CSS_SELECTOR, "button[class= 'btn btn-success']")
    enter_country = (By.CSS_SELECTOR, "input[id='country']")
    wait_country = (By.CSS_SELECTOR, "div[class='suggestions']")

    def __init__(self, driver):
        self.driver = driver

    def click_Success_checkOutButton(self):
        return self.driver.find_element(*ConfirmPage.Success_checkout_button)

    def enter_country_name(self):
        return self.driver.find_element(*ConfirmPage.enter_country)

    def wait_country_click(self):
        return self.driver.find_element(*ConfirmPage.wait_country)

