from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    card_title = (By.CSS_SELECTOR, "h4[class = 'card-title' ]")
    add_button = (By.XPATH, "(//button[@class = 'btn btn-info' ])[4]")
    checkOutButton = (By.CSS_SELECTOR, "a[class = 'nav-link btn btn-primary' ]")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.card_title)

    def addToCart(self):
        return self.driver.find_element(*CheckOutPage.add_button)

    def clickcheckOutButton(self):
        self.driver.find_element(*CheckOutPage.checkOutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage