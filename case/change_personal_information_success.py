'''
    已有账号:
    "用户名：user松1
    email:user11@qq.com
    密码：123456
    确认密码：123456
    手机：13912345678
预置条件:
    1.打开谷歌浏览器
    2.进入登录页面--> http://localhost:8080/ecshop/
步骤:
    1.点击用户中心
    2.检查是否进入用户中心
预期:
    页面显示当前位置为 首页>用户中心
'''
import unittest, time
from common.base import open_browser, Base
from page.personal_information_page import PersonalInformationPage
from page.login_page import login_url, LoginPage
from common.database import Database



class PersonalInformation(unittest.TestCase):
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

    def test_1(self):
        # 点击用户中心
        self.pip = PersonalInformationPage(self.driver)
        self.pip.click_Usercenter()
        # 检查是否进入用户中心
        text = self.pip.check_Usercenter()
        self.assertEqual("用户中心", text)

    def test_2(self):
        '''
        判断修改合理数据,后台是否成功修改
        :return:
        '''
        # 点击用户中心
        self.pip = PersonalInformationPage(self.driver)
        self.pip.click_Usercenter()
        # 点击用户信息
        self.pip.click_userinfomation()
        # 修改用户信息
        self.pip.input_old_password("2298651")
        new_pd = "2298651"
        self.pip.input_new_password(new_pd)
        self.pip.input_comfirm_password(new_pd)
        # 点击保存
        self.pip.click_comfirm_submit2()
        # 查看数据库
        db = Database("ecshop", "song2298651")
        data = db.read_one("select * from ecs_users where user_name='song'")
        # 获取password密码
        old_pd = data["password"]
        pd2 = self.bs.get_hashlib(new_pd)
        # 断言
        self.assertEqual(pd2, old_pd)


if __name__ == '__main__':
    unittest.main()
