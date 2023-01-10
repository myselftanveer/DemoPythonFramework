from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    conutry = (By.ID, "country")
    selectCountry = (By.LINK_TEXT, "India")
    # clickCountry = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    alertMsg = (By.CLASS_NAME, "alert-success")

    # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    # self.driver.find_element(By.LINK_TEXT, "India").click()
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    # successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.conutry).send_keys("ind")

    def selectCountryName(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def submitBtn(self):
        self.driver.find_element(*ConfirmPage.submit).click()

    def getAlertMsg(self):
        return self.driver.find_element(*ConfirmPage.alertMsg)
