from common.base import Base
from selenium.webdriver.common.by import By

personal_information_url = "http://localhost:8080/ecshop/"


class PersonalInformationPage(Base):
    usercenter_addr = (By.LINK_TEXT, "用户中心")
    userinfomation_addr = (By.CSS_SELECTOR, "[href='user.php?act=profile']")
    check_usercenter_addr = (By.LINK_TEXT, "用户中心")
    old_password_addr = (By.CSS_SELECTOR, "[name='old_password']")
    new_password_addr = (By.CSS_SELECTOR, "[name='new_password']")
    comfirm_password_addr = (By.CSS_SELECTOR, "[name = 'comfirm_password']")
    comfirm_submit_addr = (By.CSS_SELECTOR, "form[name='formPassword'] input[name='submit'] ")
    hint_addr = (By.CSS_SELECTOR, "[style='font-size: 14px; font-weight:bold; color: red;']")

    def click_Usercenter(self):
        self.click_element(self.usercenter_addr)

    def click_userinfomation(self):
        self.click_element(self.userinfomation_addr)

    def check_Usercenter(self):
        return self.get_element_text(self.check_usercenter_addr, timeout=10)

    def input_old_password(self, text):
        self.send_keys_element(self.old_password_addr, text=text)

    def input_new_password(self, text):
        self.send_keys_element(self.new_password_addr, text=text)

    def input_comfirm_password(self, text):
        self.send_keys_element(self.comfirm_password_addr, text=text)

    def click_comfirm_submit2(self):
        self.click_element(self.comfirm_submit_addr)

    def get_hint_text(self):
        return self.get_element_text(self.hint_addr)

    def click_alert(self):
        return self.driver.switch_to.alert

    def accept_alert(self):
        self.click_alert().accept()