from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name='name")
    email = (By.NAME, "email")
    check = (By.ID,"exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    successmessage =  (By.CLASS_NAME, "alert-success")
    password = (By.ID, "exampleInputPassword1")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage  = CheckoutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheck(self):
        return self.driver.find_element(*HomePage.check)

    def getSucMes(self):
        return self.driver.find_element(*HomePage.successmessage)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)