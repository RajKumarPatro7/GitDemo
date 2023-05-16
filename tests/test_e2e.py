from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_one(BaseClass):
    def test_e2e(self):
        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()

        products = checkOutPage.getCardTitle()
        for i in products:
            if i.text == 'Blackberry':
                log.info(i.text)
                checkOutPage.addToCart().click()

        confirmPage = checkOutPage.clickcheckOutButton()
        confirmPage.click_Success_checkOutButton().click()
        log.info("Entering country ")
        confirmPage.enter_country_name().send_keys("India")
        self.verifyLinkPresence(ConfirmPage.wait_country)
        confirmPage.wait_country_click().click()

        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[class = 'btn btn-success btn-lg']").click()
        message = self.driver.find_element(By.XPATH, "//div[@class= 'alert alert-success alert-dismissible']").text
        assert "×\nSuccess! Thank you! Your order will be delivered in next few weeks :-)." in message, "Validation " \
                                                                                                        "Failed"
