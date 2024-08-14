from common.base import Base
from selenium.webdriver.common.by import By

personal_information_url = "http://localhost:8080/ecshop/"


class PersonalInformationPage(Base):
    shouhuodizhi = (By.PARTIAL_LINK_TEXT, "收货地址")
    shouhuorenxinxi = (By.LINK_TEXT, "收货人信息")
    name_addr_1 = (By.CSS_SELECTOR, '#consignee_0')
    email_addr_1 = (By.CSS_SELECTOR, '#email_0')
    receiving_addr_1 = (By.CSS_SELECTOR, '#address_0')
    postal_addr_1 = (By.CSS_SELECTOR, '#zipcode_0')
    tel_addr_1 = (By.CSS_SELECTOR, '#tel_0')
    phone_addr_1 = (By.CSS_SELECTOR, '#mobile_0')
    check_submit_1 = (By.CSS_SELECTOR, ".bnt_blue_1")
    shanchu = (By.CSS_SELECTOR, ".bnt_blue")
    add_receiving_submit_1 = (By.CSS_SELECTOR, ".bnt_blue_2")
    name_addr_2 = (By.CSS_SELECTOR, '#consignee_1')
    email_addr_2 = (By.CSS_SELECTOR, '#email_1')
    receiving_addr_2 = (By.CSS_SELECTOR, '#address_1')
    postal_addr_2 = (By.CSS_SELECTOR, '#zipcode_1')
    tel_addr_2 = (By.CSS_SELECTOR, '#tel_1')
    phone_addr_2 = (By.CSS_SELECTOR, '#mobile_1')

    def input_name_1(self, name):
        self.send_keys_element(self.name_addr_1, name)

    def input_email_1(self, email):
        self.send_keys_element(self.email_addr_1, email)

    def input_receiving_1(self, receiving):
        self.send_keys_element(self.receiving_addr_1, receiving)

    def input_postal_1(self, postal):
        self.send_keys_element(self.postal_addr_1, postal)

    def input_tel_1(self, tel):
        self.send_keys_element(self.tel_addr_1, tel)

    def input_phone_1(self, phone):
        self.send_keys_element(self.phone_addr_1, phone)

    def click_check_submit_1(self):
        self.click_element(self.check_submit_1)

    def click_add_receiving_submit_1(self):
        self.click_element(self.add_receiving_submit_1)

    def input_name_2(self, name):
        self.send_keys_element(self.name_addr_2, name)

    def input_email_2(self, email):
        self.send_keys_element(self.email_addr_2, email)

    def input_receiving_2(self, receiving):
        self.send_keys_element(self.receiving_addr_2, receiving)

    def input_postal_2(self, postal):
        self.send_keys_element(self.postal_addr_2, postal)

    def input_tel_2(self, tel):
        self.send_keys_element(self.tel_addr_2, tel)

    def input_phone_2(self, phone):
        self.send_keys_element(self.phone_addr_2, phone)

    def click_shouhuodizhi(self):
        self.click_element(self.shouhuodizhi)

    def element_shouhuorenxinxi(self):
        return self.find_element(self.shouhuorenxinxi)

    def click_shanchu(self):
        self.click_element(self.shanchu)
