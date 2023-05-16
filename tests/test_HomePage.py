import time

import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_HomePage(BaseClass):

    def test_form_Submittion(self, data_load):
        homePage = HomePage(self.driver)
        homePage.name_field().send_keys(data_load[0])
        homePage.email_field().send_keys(data_load[1])
        homePage.pass_field().send_keys(data_load[2])
        self.selectOptionbyIndex(homePage.gender_select(), 1)
        homePage.select_employee_status().click()
        homePage.click_submit().click()
        success_text = "×\nSuccess! The Form has been submitted successfully!."
        assert success_text == homePage.success_message().text, "This test is Failed"
        self.driver.refresh()

    @pytest.fixture(params=[("Rahul", "Rahul@123gmail.com", "Rahul"), ("Raj", "raj123@gmail.com", "Raj")])
    def data_load(self, request):
        return request.param
