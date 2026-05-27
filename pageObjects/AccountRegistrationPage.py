from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "_R_1h6kqsqppb6amH1_"
    txt_telphone_name = "telephone"
    txt_password_name = "_R_1hmkqsqppb6amH1_"
    txt_confpassword_name = "confirm"
    chk_policy_name = "agree"
    btn_cont_xpath = "//div[@class='x1ja2u2z x78zum5 x2lah0s x1n2onr6 xl56j7k x6s0dn4 xozqiw3 x1q0g3np x972fbf x10w94by x1qhh985 x14e42zd x9f619 xtvsq51 xqbgfmv xbe3n85 x7a1id4 x1d9i5bo x1xila8y x1bumbmr xc8cyl1']"
    text_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    # def setFirstName(self,fname):
    #   self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)
    #
    # def setLastName(self,lname):
    #     self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_name).send_keys(email)

    # def setTelephone(self,tel):
    #    self.driver.find_element(By.NAME,self.txt_telphone_name).send_keys(tel)

    def setPassword(self, pwd):
        self.driver.find_element(By.ID, self.txt_password_name).send_keys(pwd)

    # def setConfirmPassword(self,cnfpwd):
    #     self.driver.find_element(By.NAME,self.txt_confpassword_name).send_keys(cnfpwd)

    # def setPrivacyPolicy(self):
    #     self.driver.find_element(By.NAME,self.chk_policy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()

    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_xpath).text
        except:
            None
