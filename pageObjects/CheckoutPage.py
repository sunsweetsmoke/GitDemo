import time
from operator import truediv

from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class CheckoutPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    phoneCard = (By.XPATH, "//app-card")
    buttonAdd = (By.CSS_SELECTOR, ".btn-info")
    btnGoToCheckout = (By.CSS_SELECTOR, ".btn-primary")
    btnGoToDelivery = (By.CSS_SELECTOR, ".btn-success")

    def getCards(self):
        log = self.getlogger()
        log.info("im in getcards \n I found 4 cards with titles: \n")
        cards = self.driver.find_elements(*CheckoutPage.phoneCard)
        for card in cards:
            log.info(card.find_element(By.CSS_SELECTOR, ".card-title a").text)
        return cards

    def getButtonAddfromCard(self, card):
        return card.find_element(*CheckoutPage.buttonAdd)

    def searchByTitle(self,card,cardname):
        foundByTitle = False
        if card.find_element(By.CSS_SELECTOR, ".card-title a").text == cardname:
            foundByTitle = True
        return foundByTitle

    def goToCheckout(self):
        return self.driver.find_element(*CheckoutPage.btnGoToCheckout)

    def checkCart(self):
        log = self.getlogger()
        log.info("Checkig if the button Remove exists ... \n")
        if self.driver.find_element(By.CSS_SELECTOR,".btn-danger"):
            log.info("Checkout page is OK. You can continue\n")
        else:
            log.info("THERE IS NO REMOVE BUTTON YOU DIDNT ADD ANYTHING\n")

    def goToDelivery(self):
        return self.driver.find_element(*CheckoutPage.btnGoToDelivery)