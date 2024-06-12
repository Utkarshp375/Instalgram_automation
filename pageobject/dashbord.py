from selenium.webdriver.common.by import By
class Dasbord:
    def __init__(self,driver):
        self.driver=driver
    message_xpath ="//span[contains(text(),'Messages')]"
    send_button_xpath = "//div[contains(text(),'Send message')]"
    username_xpath ="//input[@placeholder='Search...']"
    username_click_xpath ="//body[1]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/label[1]/div[1]/input[1]"
    chat_click_xpath ="//div[contains(text(),'Chat')]"
    send_message_xpath ="//p[@class='xat24cr xdj266r']"
    sendfinal_xpath ="//div[normalize-space()='Send']"
    seatting_xpath ="(//*[name()='svg'][@aria-label='Settings'])[1]"
    logout_xpath ="//span[contains(text(),'Log out')]"

    def message(self):
        self.driver.find_element(By.XPATH,self.message_xpath).click()
    def send(self):
        self.driver.find_element(By.XPATH,self.send_button_xpath).click()
    def search_username(self,user):
        self.driver.find_element(By.XPATH,self.username_xpath).send_keys(user)
    def clic(self):
        self.driver.find_element(By.XPATH,self.username_click_xpath).click()
    def chat(self):
        self.driver.find_element(By.XPATH,self.chat_click_xpath).click()
    def sendd(self,sendmess):
        self.driver.find_element(By.XPATH,self.send_message_xpath).send_keys(sendmess)
    def se(self):
        self.driver.find_element(By.XPATH,self.sendfinal_xpath).click()
    def set(self):
        self.driver.find_element(By.XPATH,self.seatting_xpath).click()
    def logout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()

