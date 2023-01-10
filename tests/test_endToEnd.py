from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_Ecommerce(BaseClass):

    def test_end2end(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()

        cards = checkoutpage.getCardTitles()
        log.info("Get All Product List")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()
                checkoutpage.checkOutItems()
        confirmPage = checkoutpage.checkOutSuccess()
        confirmPage.getCountryName()
        self.verifyLinkPresence("India")
        confirmPage.selectCountryName().click()
        confirmPage.getCheckBox().click()
        confirmPage.submitBtn()
        alertMessage = confirmPage.getAlertMsg().text
        log.info("Alert Message is" + alertMessage)
        assert "Success! Thank you!" in alertMessage
