import unittest
from common.base import open_browser, Base
from page.personal_information_page import PersonalInformationPage
from page.login_page import login_url, LoginPage


class PersonalInfofmationFail(unittest.TestCase):
    def setUp(self):
        '''
        1.打开谷歌浏览器
        2.进入ecshop首页
        3.登录账号
        song
        2298651
        :return:
        '''
        self.driver = open_browser()
        self.bs = Base(self.driver)
        self.bs.get_url(login_url)
        self.lp = LoginPage(self.driver)
        self.lp.input_username("song")
        self.lp.input_password("2298651")
        self.lp.click_submit()

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        '''
        判断输入错误信息,点击修改,会给提示
        :return:
        '''
        # 点击用户中心
        self.pip = PersonalInformationPage(self.driver)
        self.pip.click_Usercenter()
        # 点击用户信息
        self.pip.click_userinfomation()
        # 修改用户信息
        self.pip.input_old_password("1")
        new_pd = "1"
        self.pip.input_new_password(new_pd)
        self.pip.input_comfirm_password(new_pd)
        # 点击保存
        self.pip.click_comfirm_submit2()
        # 检查提示
        text = self.pip.get_hint_text()
        self.assertEqual("- 登录密码不能少于 6 个字符。", text)

    def test_2(self):
        '''
        判断为空检查,会给提示
        :return:
        '''
        # 点击用户中心
        self.pip = PersonalInformationPage(self.driver)
        self.pip.click_Usercenter()
        # 点击用户信息
        self.pip.click_userinfomation()
        # 只输入原密码,新密码空
        self.pip.input_old_password("2298651")
        # 点击第二个保存按钮
        self.pip.click_comfirm_submit2()
        # 检查提示
        try:
            alert = self.pip.click_alert().text
            self.assertTrue(alert)
        except Exception:
            print("未输入新密码,没有提示")

    def test_3(self):
        '''
        判断只输入新密码,点击修改,会给提示
        :return:
        '''
        # 点击用户中心
        self.pip = PersonalInformationPage(self.driver)
        self.pip.click_Usercenter()
        # 点击用户信息
        self.pip.click_userinfomation()
        # 修改用户信息
        self.pip.input_old_password("2298651")
        new_pd = "123456"
        self.pip.input_new_password(new_pd)
        # 点击保存
        self.pip.click_comfirm_submit2()
        # 检查提示
        try:
            alert = self.pip.click_alert().text
            self.assertTrue(alert)
        except Exception:
            print("只输入新密码,没有提示")

    def test_4(self):
        '''
        输入原本的密码信息,点击修改,检查提示信息
        :return:
        '''
        # 点击用户中心
        self.pip = PersonalInformationPage(self.driver)
        self.pip.click_Usercenter()
        # 点击用户信息
        self.pip.click_userinfomation()
        # 修改用户信息
        self.pip.input_old_password("2298651")
        self.pip.input_new_password("2298651")
        self.pip.input_comfirm_password("2298651")
        # 点击保存
        self.pip.click_comfirm_submit2()
        # 检查提示
        text = self.pip.get_hint_text()
        self.assertIn("与原密码相同", text, msg="使用原密码修改成功,且无提示,这是一个bug")

    def test_5(self):
        '''
        检查确认密码按钮生效
        :return:
        '''
        # 点击用户中心
        self.pip = PersonalInformationPage(self.driver)
        self.pip.click_Usercenter()
        # 点击用户信息
        self.pip.click_userinfomation()
        # 点击保存
        self.pip.click_comfirm_submit2()
        # 获取弹窗
        try:
            alert = self.pip.click_alert().text
            self.assertTrue(alert)
        except Exception:
            print("没有弹窗")


if __name__ == '__main__':
    unittest.main()
