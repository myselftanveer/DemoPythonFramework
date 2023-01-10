from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOutSccess = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkOutBtn).click()

    def checkOutSuccess(self):
        self.driver.find_element(*CheckoutPage.checkOutSccess).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

    # products = (By.XPATH, "//div[@class='card h-100']")
    # productName = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    # productBtn = (By.XPATH, "//div[@class='card h-100']/div/button")
    # checkoutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    # checkoutSuccess = (By.XPATH, "//button[@class='btn btn-success']")
    #
    # def getProducts(self):
    #     return self.driver.find_elements(*CheckoutPage.products)
    #
    # def getProdName(self):
    #     return self.driver.find_elements(*CheckoutPage.productName)
    #
    # def getProdBtn(self):
    #     return self.driver.find_element(*CheckoutPage.productBtn).click()
    #
    # def getCheckoutBtn(self):
    #     return self.driver.find_element(*CheckoutPage.checkoutBtn)
    #
    # def getCheckoutSuccess(self):
    #     return self.driver.find_element(*CheckoutPage.checkoutSuccess)
