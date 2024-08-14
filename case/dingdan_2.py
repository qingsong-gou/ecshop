'''
该账户已有下 相机订单,炫彩翻页保护套订单
账号:user2
密码:123456
'''
import unittest, time
from common.base import open_browser, Base
from page.dingdan_page import DingDanPage
from page.login_page import login_url, LoginPage
from page.chongzhi_page import JiaoYi


class DingDanXinXi(unittest.TestCase):
    def setUp(self):
        # 打开谷歌浏览器
        self.driver = open_browser()
        # 进入登录页面
        self.bs = Base(self.driver)
        self.bs.get_url(login_url)
        # 输入账户
        self.lp = LoginPage(self.driver)
        self.lp.input_username("user2")
        self.lp.input_password("123456")
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

    # def test_01(self):
    #     '''
    #     点击订单号,跳转到订单信息
    #     :return:
    #     '''
    #     # 点击订单号
    #     self.ddp.click_dingdanhao_1()
    #     # 检查跳转
    #     try:
    #         text = self.ddp.element_dingdanzhuangtai_1()
    #     except Exception as e:
    #         pass
    #     else:
    #         self.assertIsNotNone(text, msg="获取不到跳转页面后的'订单状态',跳转失败")

    # def test_2(self):
    #     '''
    #     点击取消订单,弹出提示框
    #     :return:
    #     '''
    #     # 点击取消订单
    #     self.ddp.click_quxiaodingdan()
    #     # 获取弹窗
    #     try:
    #         alert = self.driver.switch_to.alert
    #     except Exception as e:
    #         pass
    #     else:
    #         self.assertIsNotNone(alert, msg="点击取消订单,获取不到提示弹窗")
    #
    # def test_3(self):
    #     '''
    #     点击再次购买,跳转到购物车
    #     :return:
    #     '''
    #     self.ddp.click_zaicigoumai()
    #     try:
    #         text = self.ddp.get_zhinengxiangji_text()
    #     except Exception as e:
    #         pass
    #     else:
    #         self.assertEqual("智能相机", text, msg="跳转的页面没有获取到'智能相机'元素,再次购买按钮跳转"
    #                                            "失败")

    def test_4(self):
        '''
        验证合并后订单号减少一个
        :return:
        '''


if __name__ == '__main__':
    unittest.main()
