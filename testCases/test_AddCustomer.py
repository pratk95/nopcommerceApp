import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("******* Test_003_AddCustomer *********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* Login Successful *********")

        self.logger.info("********* Starting Add customer test *********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        time.sleep(3)
        self.addcust.clickonCustomersMenuItem()
        time.sleep(3)
        self.addcust.clikOnAddnew()

        self.logger.info("********** Providing customer Info **************")

        self.email = random_generator()+"@gamil.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomRoles("Guests")
        self.addcust.setMangerOfVender("Vendor 2")
        self.addcust.setGender('Male')
        self.addcust.setFirstName('Demo')
        self.addcust.setLastName('Test')
        self.addcust.setDOB("2/7/1999") # format: MM/DD/YYYY
        self.addcust.setCompanyName("DemoQA")
        self.addcust.setAdminContent("Testing Purpose ........")
        self.addcust.clickOnSave()

        self.logger.info("********** Saving customer info")

        self.logger.info("************ Add customer validation started ***********")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        # print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("*********** Add customer test Passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.info("********** Add customer test Failed *************")
            assert False

        self.driver.close()
        self.logger.info("*********** Ending Add customer test ***********")
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))