import time

import pytest
from pyexpat.errors import messages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.getCheck().click()
        homepage.getEmail().send_keys(getData["email"])
        self.selectOptionByText(homepage.getGender(),getData["gender"])
        homepage.getSubmit().click()
        print(homepage.driver.title)
        print(homepage.driver.current_url)
        #driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
        #driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
        #driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
        message = homepage.getSucMes().text
        #message = driver.find_element(By.CLASS_NAME, "alert-success").text

        print(message)
        assert "Success" in message
        time.sleep(3)
        homepage.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestDataFromXls("Testcase2"))
    def getData(self, request):
        return request.param