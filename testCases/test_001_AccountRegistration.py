import time

import pytest
import self

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import os

from utilities import randomeString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.sanity
class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() # For logging

    def test_account_reg(self,setup):
        self.logger.info("Execution started")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching")
        self.driver.maximize_window()
        time.sleep(2)
        # self.hp=HomePage(self.driver)
        # self.hp.clickMyAccount()
        # self.hp.clickRegister()
        self.regpage=AccountRegistrationPage(self.driver)
        time.sleep(2)
        # self.regpage.setFirstName("John")
        # self.regpage.setLastName("Canedy")
        #self.regpage.setEmail("abc1991@gmail.com")
        # self.email=randomeString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        time.sleep(2)
        # self.regpage.setTelephone("65656565")
        self.regpage.setPassword(self.password)
        time.sleep(2)
        #self.regpage.setConfirmPassword("abcxyz")
        #self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        time.sleep(2)
        self.logger.info("Account Has Been Created")
        time.sleep(2)
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png")
        time.sleep(2)
        #self.confmsg=self.regpage.getconfirmationmsg()
        self.driver.close()
        # if self.confmsg == "Your Account Has Been Created!":
        #     self.logger.info("Account Has Been Created")
        #     assert True
        # else:
        #     self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
        #     self.driver.close()
        #     assert False
        #     self.logger.info("Account Has NOT Been Created")






