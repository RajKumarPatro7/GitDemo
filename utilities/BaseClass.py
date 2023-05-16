import inspect
import logging

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import logging
import inspect

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
    def verifyLinkPresence(self, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(text))

    def selectOptionbyIndex(self, locator, val):
        select = Select(locator)
        select.select_by_index(val)
