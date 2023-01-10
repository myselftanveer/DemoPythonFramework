import pytest
from selenium.webdriver.common.by import By

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_HomePage(BaseClass):

    def test_formSubmission(self, getData):
        homePage = HomePage(self.driver)
        log = self.getLogger()
        # homePage.getName().send_keys(getData[0])
        # homePage.getEmail().send_keys(getData[1])
        # homePage.getPwd().send_keys(getData[2])
        # homePage.getCheck().click()
        # self.selectOptionByText(homePage.getGender(), getData[3])
        # homePage.getSubmit().submit()
        # assert "Success" in homePage.getAlert().text
        # self.driver.refresh()

        # @pytest.fixture(params=[("xyz", "xyz@yopmail.com", "123456", "Male"), ("xyz7", "xyz7@yopmail.com", "12345678", "Female")])
        # def getData(self, request):
        #     return request.param
        log.info("First Name is" + getData["fName"])
        homePage.getName().send_keys(getData["fName"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPwd().send_keys(getData["pwd"])
        homePage.getCheck().click()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.getSubmit().submit()
        assert "Success" in homePage.getAlert().text
        self.driver.refresh()

    # @pytest.fixture(params=HomePageData.test_HomePage_data)
    # def getData(self, request):
    #     return request.param
    @pytest.fixture(params=HomePageData.getTestData("Valid"))
    def getData(self, request):
        return request.param