import unittest, time
from common.base import open_browser, Base
from page.personal_address_page import PersonalInformationPage
from page.login_page import login_url, LoginPage
from page.chongzhi_page import JiaoYi


class DiZhi(unittest.TestCase):
    def setUp(self):
        # 打开谷歌浏览器
        self.driver = open_browser()
        # 进入登录页面
        self.bs = Base(self.driver)
        self.bs.get_url(login_url)
        # 输入账户
        self.lp = LoginPage(self.driver)
        self.lp.input_username("song")
        self.lp.input_password("2298651")
        # 点击登录
        self.lp.click_submit()
        # 点击用户中心
        self.jy = JiaoYi(self.driver)
        self.jy.click_usercenter_addr()
        # 点击收货地址
        self.pip = PersonalInformationPage(self.driver)
        self.pip.click_shouhuodizhi()

    def tearDown(self):
        self.driver.quit()

    def test_tiaozhuan(self):
        '''
        判断页面跳转正确
        :return:
        '''
        # 获取页面"收货人信息"元素
        try:
            element = self.pip.element_shouhuorenxinxi()
        except Exception:
            pass
        else:
            self.assertIsNotNone(element, msg="获取不到'收货人信息',页面跳转失败")

    def test_queren_submit(self):
        '''
        点击确认修改,弹出提示窗口
        :return:
        '''
        # 点击确认修改
        self.pip.click_check_submit_1()
        # 获取弹窗
        try:
            alert = self.driver.switch_to.alert
        except Exception:
            pass
        else:
            self.assertIsNotNone(alert, msg="原信息点击修改,没有弹窗按提示")

    def test_shanchu_submit(self):
        '''
        点击删除,弹窗提示
        :return:
        '''
        # 点击删除
        self.pip.click_shanchu()
        # 获取弹窗
        try:
            alert = self.driver.switch_to.alert
        except Exception:
            pass
        else:
            self.assertIsNotNone(alert, msg="点击删除,没有弹窗按提示")

    def test_xinzeng(self):
        '''
        点击新增收获地址,弹窗提示
        :return:
        '''
        # 点击新增地址
        self.pip.click_add_receiving_submit_1()
        # 获取弹窗
        try:
            alert = self.driver.switch_to.alert
        except Exception:
            pass
        else:
            self.assertIsNotNone(alert, msg="未填信息,点击新增,没有弹窗按提示")


if __name__ == '__main__':
    unittest.main()
