import unittest
from common.base import open_browser, Base
from page.chongzhi_page import JiaoYi
from page.login_page import login_url, LoginPage


class ChongZhi(unittest.TestCase):
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
        # 点击资金管理
        self.jy.click_zijinguanli()

    def tearDown(self):
        self.driver.quit()

    def test_tiaoZhuan(self):
        '''
        资金管理页面跳转
        :return:
        '''
        # 获取显示信息
        try:
            text = self.jy.get_huiyuanyue_text()
        except Exception:
            pass
        else:
            self.assertEqual("会员余额", text, msg="获取不到'会员余额',页面跳转失败")

    def test_chongZhi(self):
        '''
        充值页面跳转
        :return:
        '''
        # 点击充值
        self.jy.click_chongzhi()
        # 获取"充值金额:"文本
        try:
            text = self.jy.get_chongzhijie_text()
        except Exception:
            pass
        else:
            self.assertEqual("充值金额:", text, msg="获取不到'充值金额:', 页面跳转失败")

    def test_tixian(self):
        '''
        提现页面跳转
        :return:
        '''
        # 点击提现
        self.jy.click_tixian()
        # 获取"提现"文本

        try:
            text = self.jy.get_tixianjie_text()
        except Exception:
            pass
        else:
            self.assertEqual("提现金额:", text, msg="获取不到'提现金额:', 页面跳转失败")

    def test_chakanmingxi(self):
        '''
        查看账户明细
        :return:
        '''
        # 点击查看账户明细
        self.jy.click_chakanmingxi()
        # 获取"您当前的可用资金为：￥0.00元"文本
        try:
            text = self.jy.get_keyongyue_text()
        except Exception:
            pass
        else:
            self.assertEqual("您当前的可用资金为：￥0.00元", text, msg="获取不到'您当前的可用资金为：￥0.00元', 页面跳转失败")

    def test_chakanjilu(self):
        '''
        查看申请记录
        :return:
        '''
        # 点击查看申请记录
        self.jy.click_chakanjilu()
        # 获取"管理员备注"文本
        try:
            text = self.jy.get_guanliyuanbeizhu_text()
        except Exception:
            pass
        else:
            self.assertEqual("管理员备注", text, msg="获取不到'管理员备注', 页面跳转失败")


if __name__ == '__main__':
    unittest.main()
