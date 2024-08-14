"""
用例id: ECSHOP_ST_ADDERSSEDIT_004  (合法数据)
        ECSHOP_ST_ADDERSSEDIT_005-ECSHOP_ST_ADDERSSEDIT_013(非法数据)
        ECSHOP_ST_ADDERSSEDIT_014   (确认修改)
步骤:
    1. 打开网页 ; http://localhost:8080/ecshop/
    2. 点击登录按钮
    3. 输入用户名密码后点击登录 : user/user123456
    4.点击用户中心
    5.点击收货地址
    6.输入数据
    7.点击确定
"""
import unittest

from common.database import Database
from common.base import open_browser
from page.login_page import LoginPage, login_url
from common.openExcel import OpenExcel
from page.chongzhi_page import JiaoYi
from page.personal_address_page import *
import ddt
import os
from time import sleep

ot = OpenExcel(os.path.split(__file__)[0] + r"/testdata/address_success.xlsx",
               converters={"zipcode": str, "tel": str, "mobile": str})
data1 = ot.read_list()
ot = OpenExcel(os.path.split(__file__)[0] + r"/testdata/address_fail.xlsx",
               converters={"country": str, "zipcode": str, "tel": str, "mobile": str})
data2 = ot.read_list()


@ddt.ddt()
class UserInfoCase(unittest.TestCase):
    def setUp(self):
        # 1. 打开网页 ; http://ecshop.itsoso.cn/  首页
        # 打开浏览器
        self.driver = open_browser()
        self.lp = LoginPage(self.driver)  # 实例化 首页的对象
        self.lp.get_url(login_url)
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
        self.driver.close()

    @ddt.data(*data1)
    def test_address_success(self, data):
        """
        合法数据修改地址成功
        :param data:
        :return:
        """
        # 选择国家,省,市,地区
        self.addr.selectCountries(1)
        self.addr.selectProvinces(23)
        self.addr.selectCities(1)
        self.addr.selectDistricts(1)
        # 输入收货人姓名
        self.addr.clearConsign()
        self.addr.inputConsign(data[0])
        # 输入邮件地址
        self.addr.clearEmail()
        self.addr.inputEmail(data[1])
        # 修改详细地址
        self.addr.clearAddress_0()
        self.addr.inputAddress_0(data[2])
        # 修改邮政编码
        self.addr.clearZipcode_0()
        self.addr.inputZipcode_0(data[3])
        # 修改电话
        self.addr.clearTel_0()
        self.addr.inputTel_0(data[4])
        # 修改手机
        self.addr.clearMobile_0()
        self.addr.inputMobile_0(data[5])
        # 点击确认修改
        self.addr.clickSubmit_0()
        # # sleep(10)
        # # 定位弹窗
        try:
            self.addr.getAlertText()  # 定位弹窗失败,修改成功
        except Exception as e:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    @ddt.data(*data2)
    def test_address_fail(self, data):
        """
        非法数据修改地址失败
        :param data:
        :return:
        """
        # 选择国家,省,市,地区
        self.addr.selectCountries(data[0])
        try:
            self.addr.selectProvinces(1)
            self.addr.selectCities(1)
            self.addr.selectDistricts(1)
        except Exception:
            pass
        # 输入收货人姓名
        self.addr.clearConsign()
        self.addr.inputConsign(data[1])
        # 输入邮件地址
        self.addr.clearEmail()
        self.addr.inputEmail(data[2])
        # 修改详细地址
        self.addr.clearAddress_0()
        self.addr.inputAddress_0(data[3])
        # 修改邮政编码
        self.addr.clearZipcode_0()
        self.addr.inputZipcode_0(data[4])
        # 修改电话
        self.addr.clearTel_0()
        self.addr.inputTel_0(data[5])
        # 修改手机
        self.addr.clearMobile_0()
        self.addr.inputMobile_0(data[6])
        # 点击确认修改
        self.addr.clickSubmit_0()
        # 点击弹窗
        # 定位弹窗
        try:
            self.addr.acceptAlert()
        except Exception as e:
            pass
        # 查询数据库
        db = Database("song2298651", "ecshop_db", port=3306)
        sql = "select country,consignee,ecs_user_address.email,address,zipcode,tel,mobile from ecs_users join ecs_user_address using (user_id)where user_name='user'"
        args = None
        user = db.fetchone(sql, args)

        if user["country"] == int(data[0]) and user["consignee"] == data[1] and user["email"] == data[2] and user[
            "address"] == data[3] and user["zipcode"] == data[4] and user["tel"] == data[5] and user["mobile"] == data[
            6]:
            self.assertTrue(False, msg="修改数据成功,用例不通过")
        else:
            self.assertTrue(True)

        sleep(10)


if __name__ == "__main__":
    unittest.main()
