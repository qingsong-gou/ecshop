"""
存放的是 登录页面的 元素定位 和 元素操作
"""
from common.base import Base
from selenium.webdriver.common.by import By

login_url = "http://localhost:8080/ecshop/user.php"


class LoginPage(Base):
    username_loc = (By.CSS_SELECTOR, "input[name='username']")
    password_loc = (By.CSS_SELECTOR, "input[name='password']")
    submit_loc = (By.CSS_SELECTOR, "[name='submit']")
    web_username_loc = (By.CSS_SELECTOR, ".f4_b")

    # 输入用户名
    def input_username(self, username):
        """
        输入用户名
        :param username: 用户名
        :return:
        """
        self.send_keys_element(self.username_loc, username)

    # 输入密码
    def input_password(self, password):
        """
        输入密码
        :param password: 密码
        :return:
        """
        self.send_keys_element(self.password_loc, password)

    # 点击登录
    def click_submit(self):
        """
        点击登录
        :return:
        """
        self.click_element(self.submit_loc)

    # 获取登录后的文本
    def get_web_username(self):
        """
        获取登录后页面显示的用户名
        :return:
        """
        return self.get_element_text(self.web_username_loc)
