from common.base import Base
from selenium.webdriver.common.by import By


class JiaoYi(Base):
    zijinguanli = (By.CSS_SELECTOR, "[href='user.php?act=account_log']")
    huiyuanyue = (By.XPATH, "//span[text()='会员余额']")
    usercenter_addr = (By.LINK_TEXT, "用户中心")
    chongzhi = (By.XPATH, "//a[text()='充值']")
    chongzhijie = (By.XPATH, "//td[text()='充值金额:']")
    tixian = (By.XPATH, "//a[text()='提现']")
    tixianjie = (By.XPATH, "//td[text()='提现金额:']")
    chakanmingxi = (By.XPATH, "//a[text()='查看帐户明细']")
    keyongyue = (By.XPATH, "//td[text()='您当前的可用资金为：￥0.00元']")
    chakanjilu = (By.XPATH, "//a[text()='查看申请记录']")
    guanliyuanbeizhu = (By.XPATH, "//td[text()='管理员备注1']")

    def click_zijinguanli(self):
        self.click_element(self.zijinguanli)

    def click_usercenter_addr(self):
        self.click_element(self.usercenter_addr)

    def get_huiyuanyue_text(self):
        return self.get_element_text(self.huiyuanyue)

    def click_chongzhi(self):
        self.click_element(self.chongzhi)

    def get_chongzhijie_text(self):
        return self.get_element_text(self.chongzhijie)

    def click_tixian(self):
        self.click_element(self.tixian)

    def get_tixianjie_text(self):
        return self.get_element_text(self.tixianjie)

    def click_chakanmingxi(self):
        self.click_element(self.chakanmingxi)

    def get_keyongyue_text(self):
        return self.get_element_text(self.keyongyue)

    def click_chakanjilu(self):
        self.click_element(self.chakanjilu)

    def get_guanliyuanbeizhu_text(self):
        return self.get_element_text(self.guanliyuanbeizhu)
