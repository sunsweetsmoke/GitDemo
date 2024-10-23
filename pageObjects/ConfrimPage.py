from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass


class ConfirmPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    checkBoxIAgree = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
    btnSubmitOrder = (By.CSS_SELECTOR, "input[type='submit")

    def SetCountry(self,countryname):

        self.driver.find_element(By.ID, "country").send_keys(countryname)
        self.verifyLinkPresence(self.driver,countryname)
        self.driver.find_element(By.LINK_TEXT, countryname).click()

    def FinishDelivery(self):
        resultMessage = "I don't see success pop-up alert"
        self.driver.find_element(*ConfirmPage.checkBoxIAgree).click()
        self.driver.find_element(*ConfirmPage.btnSubmitOrder).click()
        resultMessage = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        return resultMessage