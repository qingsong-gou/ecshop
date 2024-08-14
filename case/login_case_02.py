import os
import ddt
import unittest
from common.base import open_browser
from common.openExcel import OpenExcel
from page.login_page import LoginPage, login_url

# 组装绝对路径
# print(__file__)
# print(os.path.dirname(__file__) + "/测试数据.xlsx")
data = OpenExcel(os.path.dirname(__file__) + "/测试数据.xlsx", {"password": str}).read_dict()
print(data)


@ddt.ddt
class LoginCase(unittest.TestCase):
    def setUp(self):
        # 打开谷歌浏览器
        driver = open_browser()
        # 进入ecshop的登录页面 : http://localhost:8080/ecshop/user.php
        self.lp = LoginPage(driver)
        self.lp.get_url(login_url)

    def tearDown(self):
        self.lp.quit()

    def login(self, username, password):
        # 输入用户名 : junfu
        self.lp.input_username(username)
        # 输入密码 : 123456
        self.lp.input_password(password)
        # 点击登录
        self.lp.click_submit()

        # 页面左上角显示登录的用户名,登录的用户名和输入的一致
        # 预期结果 : junfu
        # 实际结果 : 获取页面显示的用户名
        text = self.lp.get_web_username()

        self.assertEqual(username, text, msg="输入的用户名和页面登录后显示的用户名不一致!")

    @ddt.data(*data)
    def test_login_01(self, db):
        """
        用例ID : TC_LOGIN_001
        用例标题 : 验证合法数据登录成功
        用例预置条件 :
            1. 打开谷歌浏览器
            2. 进入ecshop的登录页面 : http://localhost:8080/ecshop/user.php
            3. 已有一个用户名为:junfu 密码为:123456 的用户
        用例的步骤:
            1. 输入用户名 : junfu
            2. 输入密码 : 123456
            3. 点击登录
        用例的预期结果
            页面左上角显示登录的用户名,登录的用户名和输入的一致
        """
        # print(db)
        # for i in data:  # i = {'username': 'junfu', 'password': '123456'}
        self.login(**db)

    # def test_case_02(self):
    #     """
    #     用例ID : TC_LOGIN_001
    #     用例标题 : 验证合法数据登录成功
    #     用例预置条件 :
    #         1. 打开谷歌浏览器
    #         2. 进入ecshop的登录页面 : http://localhost:8080/ecshop/user.php
    #         3. 已有一个用户名为:jun_fu 密码为:123456 的用户
    #     用例的步骤:
    #         1. 输入用户名 : jun_fu
    #         2. 输入密码 : 123456
    #         3. 点击登录
    #     用例的预期结果
    #         页面左上角显示登录的用户名,登录的用户名和输入的一致
    #     """
    #     # 输入用户名 : jun_fu
    #     self.lp.input_username("jun_fu")
    #     # 输入密码 : 123456
    #     self.lp.input_password("123456")
    #     # 点击登录
    #     self.lp.click_submit()
    #
    #     # 页面左上角显示登录的用户名,登录的用户名和输入的一致
    #     # 预期结果 : jun_fu
    #     # 实际结果 : 获取页面显示的用户名
    #     text = self.lp.get_web_username()
    #
    #     self.assertEqual("jun_fu", text, msg="输入的用户名和页面登录后显示的用户名不一致!")


if __name__ == '__main__':
    unittest.main()
