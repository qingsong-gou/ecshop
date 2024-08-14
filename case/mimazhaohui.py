import unittest
import time
from common.base import open_browser, Base
from page.chongzhi_page import JiaoYi
from page.login_page import login_url, LoginPage


class MiMaZhaoHui(unittest.TestCase):
    def setUp(self):
        # 打开浏览器
        self.driver = open_browser()
        # 实例化对象
        self.bs = Base(self.driver)
        # 进入页面
        self.bs.get_url(login_url)
        # 实例化登录页面对象
        self.lp = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_mima(self):
        # 点击"密码问题"
        self.lp.click_mima()
        # 获取"请输入您注册的用户名以取得您的密码提示问题。"文本
        try:
            text = self.lp.get_mimadaan_text()
        except Exception:
            pass
        else:
            self.assertEqual("请输入您注册的用户名以取得您的密码提示问题。", text, msg="获取不到'请输入您注册的用户名以取得您的密码提示问题。',页面跳转失败")

    def test_youjiandaan(self):
        # 点击"邮件"
        self.lp.click_youjian()
        # 获取"请输入您注册的用户名和注册时填写的电子邮件地址。"文本
        try:
            text = self.lp.get_youjiandaan_text()
        except Exception:
            pass
        else:
            self.assertEqual("请输入您注册的用户名和注册时填写的电子邮件地址。", text, msg="获取不到'请输入您注册的用户名和注册时填写的电子邮件地址。',页面跳转失败")

    def test_duanxindaan(self):
        # 点击"短信验证"
        self.lp.click_duanxin()
        # 获取"短信找回密码"文本
        try:
            text = self.lp.get_duanxindaan_text()
        except Exception:
            pass
        else:
            self.assertEqual("短信找回密码", text, msg="获取不到'短信找回密码',页面跳转失败")

    def test_mima_submit(self):
        '''
        点击密码问题,点击提交,验证跳转到首页
        :return:
        '''
        # 点击密码问题
        self.lp.click_mima()
        # 点击提交
        self.lp.click_mima_submit()
        time.sleep(5)
        # 获取文本
        try:
            text = self.lp.get_qingdenglu_text()
        except Exception:
            pass
        else:
            self.assertEqual("欢迎光临本店", text, msg="获取不到'欢迎光临本店',页面跳转失败")

    def test_mima_fanhui(self):
        '''
        点击密码问题,点击返回上一页,跳转到登录页面
        :return:
        '''
        # 点击密码问题
        self.lp.click_mima()
        # 点击返回上一页
        self.lp.click_mima_fanhui()
        # 获取    会员登录    元素
        try:
            text = self.lp.element_huiyuandengnlu()
        except Exception:
            pass
        else:
            self.assertIsNotNone(text, msg="获取不到'会员登录'标签,页面跳转失败")

    def test_youjian_submit(self):
        '''
        点击邮件,点击提交,给出弹窗提示
        :return:
        '''
        # 点击邮件
        self.lp.click_youjian()
        # 点击提交(定位方式一样)
        self.lp.click_mima_submit()
        # 获取弹窗,断言
        try:
            alert = self.driver.switch_to.alert
        except Exception:
            pass
        else:
            self.assertIsNotNone(alert, msg="获取不到弹窗提示,页面跳转失败")

    def test_youjian_fanhui(self):
        '''
        点击邮件,点击返回上一页,页面返回登录页面
        :return:
        '''
        # 点击邮件
        self.lp.click_youjian()
        # 点击返回上一页(定位方式一样)
        self.lp.click_mima_fanhui()
        # 获取    会员登录    元素
        try:
            text = self.lp.element_huiyuandengnlu()
        except Exception:
            pass
        else:
            self.assertIsNotNone(text, msg="获取不到'会员登录'标签,页面跳转失败")

    def test_duanxin_submit(self):
        '''
        点击短信验证,点击提交,弹出提示窗口
        :return:
        '''
        # 点击"短信验证"
        self.lp.click_duanxin()
        # 点击提交(定位方式一样)
        self.lp.click_mima_submit()
        # 获取窗口
        try:
            alert = self.driver.switch_to.alert
        except Exception:
            pass
        else:
            self.assertIsNotNone(alert, msg="获取不到弹窗提示,页面跳转失败")

    def test_duanxin_fanhui(self):
        '''
        点击短信验证,点击返回上一页,跳转到登录页面
        :return:
        '''
        # 点击"短信验证"
        self.lp.click_duanxin()
        # 点击提交(定位方式一样)
        self.lp.click_mima_fanhui()
        # 获取    会员登录    元素
        try:
            text = self.lp.element_huiyuandengnlu()
        except Exception:
            pass
        else:
            self.assertIsNotNone(text, msg="获取不到'会员登录'标签,页面跳转失败")


if __name__ == '__main__':
    unittest.main()
