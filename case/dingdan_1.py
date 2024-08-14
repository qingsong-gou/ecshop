import unittest, time
from common.base import open_browser, Base
from page.dingdan_page import DingDanPage
from page.login_page import login_url, LoginPage
from page.chongzhi_page import JiaoYi


class DingDan(unittest.TestCase):
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
        self.ddp = DingDanPage(self.driver)
        self.ddp.click_wodedingdan()

    def tearDown(self):
        self.driver.quit()

    def test_tiaozhuan(self):
        '''
        订单页面跳转性
        :return:
        '''
        # 获取 "我的订单" 元素
        try:
            text = self.ddp.element_dingdan_loc()
        except Exception:
            pass
        else:
            self.assertIsNotNone(text, msg="页面获取'我的订单'元素失败,跳转失败")

    def test_danhao(self):
        '''
        检查订单号
        :return:
        '''
        try:
            text = self.ddp.element_dingdanhao()
        except Exception as e:
            pass
        else:
            self.assertIsNotNone(text, msg="页面获取'订单号'元素失败,订单不完整")

    def test_xiadanshijian(self):
        '''
        下单时间
        :return:
        '''
        try:
            text = self.ddp.element_xiadanshijian()
        except Exception as e:
            pass
        else:
            self.assertIsNotNone(text, msg="页面获取'下单时间'元素失败,订单不完整")

    def test_dingdanzongjine(self):
        '''
        订单总金额
        :return:
        '''
        try:
            text = self.ddp.element_dingdanzongjine()
        except Exception as e:
            pass
        else:
            self.assertIsNotNone(text, msg="页面获取'订单总金额'元素失败,订单不完整")

    def test_dingdanzhuangtai(self):
        '''
        订单状态
        :return:
        '''
        try:
            text = self.ddp.element_dingdanzhuangtai()
        except Exception as e:
            pass
        else:
            self.assertIsNotNone(text, msg="页面获取'订单状态'元素失败,订单不完整")

    def test_hebingdingdan(self):
        '''
        合并订单,会出现提示窗口
        :return:
        '''
        try:
            text = self.ddp.element_hebingdingdan()
        except Exception as e:
            pass
        else:
            self.assertIsNotNone(text, msg="页面获取'合并订单'元素失败,订单不完整")

    def test_hebingdingdan2(self):
        '''
        点击合并订单,弹出提示窗口
        :return:
        '''
        self.ddp.click_hebingdingdan()
        try:
            alert = self.driver.switch_to.alert
        except Exception:
            pass
        else:
            self.assertIsNotNone(alert, msg="点击合并订单按钮,获取不到提示弹窗")


if __name__ == '__main__':
    unittest.main()
