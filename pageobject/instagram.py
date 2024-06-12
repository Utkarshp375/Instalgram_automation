from selenium.webdriver.common.by import By
class Login:
    def __init__(self,driver):
        self.driver=driver


    login_id_xpath = "//input[@name='username']"
    login_password_xpath = "//input[@name='password']"
    button_login_xpath = "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > main:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3)"
    not_now_xpath ="//button[@class='_a9-- _ap36 _a9_1']"
    def login(self,username):
        self.driver.find_element(By.XPATH,self.login_id_xpath).send_keys(username)
    def password(self,passw):
        self.driver.find_element(By.XPATH,self.login_password_xpath).send_keys(passw)
    def click(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_login_xpath).click()
    def notn(self):
        self.driver.find_element(By.XPATH,self.not_now_xpath).click()
