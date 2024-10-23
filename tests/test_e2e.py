import time
import pytest
from Utilities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfrimPage import ConfirmPage
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):


    def test_e2e(self):
        log  = self.getlogger()

        # //a[contains(@href,'shop')]  a[href*='shop']
        homepage = HomePage(self.driver)
        #self.driver.find_element(By.LINK_TEXT, "Shop").click()
        #homepage.shopItems().click()

        checkoutpage = homepage.shopItems()
        log.info("\n i'm in shop\n")

        #checkoutpage = CheckoutPage(self.driver)
        #phonelist = self.driver.find_elements(By.XPATH, "//app-card") or By.XPATH,"//div[@class='card h-100']
        phoneCards = checkoutpage.getCards()

        for phoneCard in phoneCards:
            if checkoutpage.searchByTitle(phoneCard,"Blackberry"):
                log.info("\n I successfully found Blackberry")
                checkoutpage.getButtonAddfromCard(phoneCard).click()

        checkoutpage.goToCheckout().click()
        time.sleep(2)
        checkoutpage.checkCart()
        checkoutpage.goToDelivery().click()

        confirmPage = ConfirmPage(self.driver)

        ConfirmPage.SetCountry(confirmPage,"Ukraine")
        alertText = ConfirmPage.FinishDelivery(confirmPage)
        log.info(alertText)
        time.sleep(3)
        assert "Success" in alertText
