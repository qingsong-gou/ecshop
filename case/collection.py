'''
用例标题: 验证收藏功能=
用例预置条件:
        1.打开谷歌浏览器
        2.进入ecshop首页
    步骤:
        1.点击商品
        2.点击收藏按钮
        3.点击(处理)弹出
        4.获取当前页面商品的 "本店售价的价格"
        5.点击用户中心
        6.点击我的收藏夹
        7.判断商品信息页面的 "本店售价的价格"和收藏夹的价格
'''
import unittest, time
from common.base import open_browser, Base
from page.login_page import LoginPage
from page.collection_page import CoolectionPage


class Collection(unittest.TestCase, LoginPage):
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
        self.bs.get_url("http://localhost:8080/ecshop/user.php")
        self.lp = LoginPage(self.driver)
        self.lp.input_username("song")
        self.lp.input_password("2298651")
        self.lp.click_submit()

    def test_one(self):
        '''
         1.点击商品
        2.点击收藏按钮
        3.点击(处理)弹出
        4.获取当前页面商品的 "本店售价的价格"
        5.点击用户中心
        6.点击我的收藏夹
        7.判断商品信息页面的 "本店售价的价格"和收藏夹的价格
        :return:
        '''
        # 点击首页
        self.cp = CoolectionPage(self.driver)
        self.cp.click_homPage()
        # 点击相机
        self.cp.click_camera_loc()
        # 获取价格
        old_price = self.cp.get_local_price()
        # 点击收藏
        self.cp.click_button()
        time.sleep(5)
        # 处理弹窗
        self.cp.click_alert().accept()
        # 点击用户中心
        self.cp.usercenter_click()
        # 点击我的收藏
        self.cp.user_collect_loc_click()
        # 获取价格
        new_price = self.cp.get_local_price2()
        # 断言
        self.assertEqual(old_price, new_price)


if __name__ == '__main__':
    unittest.main()
