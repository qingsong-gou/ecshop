from common.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DingDanPage(Base):
    wodedingdan = (By.LINK_TEXT, "我的订单")
    dingdan_loc = (By.CSS_SELECTOR, "span[text()='我的订单']")
    dingdanhao = (By.CSS_SELECTOR, "[text()='订单号']")
    xiadanshijian = (By.CSS_SELECTOR, "[text()='下单时间']")
    dingdanzongjine = (By.CSS_SELECTOR, "[text()='订单总金额']")
    dingdanzhuangtai = (By.CSS_SELECTOR, "[text()='订单状态']")
    hebingdingdan = (By.CSS_SELECTOR, ".bnt_blue_1")
    dingdanhao_1 = (By.CSS_SELECTOR, "[href='user.php?act=order_detail&order_id=11']")
    quxiaodingdan = (By.LINK_TEXT, "取消订单")
    zaicigoumai = (By.LINK_TEXT, "再次购买")
    dingdanzhuangtai_1 = (By.XPATH, "//span[text()='订单状态']")
    zhinengxiangji = (By.LINK_TEXT, "智能相机")
    zhuxiala = (By.CSS_SELECTOR, "[name='to_order']")
    congxiala = (By.CSS_SELECTOR, "[name='from_order']")

    def click_wodedingdan(self):
        self.click_element(self.wodedingdan)

    def select_zhuxiala(self, index):
        return self.xiala(self.zhuxiala, index)

    def select_congxiala(self, index):
        return self.xiala(self.congxiala, index)

    def element_dingdan_loc(self):
        return self.find_element(self.dingdan_loc)

    def element_dingdanhao(self):
        return self.find_element(self.dingdanhao)

    def element_xiadanshijian(self):
        return self.find_element(self.xiadanshijian)

    def element_dingdanzongjine(self):
        return self.find_element(self.dingdanzongjine)

    def element_dingdanzhuangtai(self):
        return self.find_element(self.dingdanzhuangtai)

    def element_hebingdingdan(self):
        return self.find_element(self.hebingdingdan)

    def click_hebingdingdan(self):
        self.click_element(self.hebingdingdan)

    def click_dingdanhao_1(self):
        self.click_element(self.dingdanhao_1)

    def click_quxiaodingdan(self):
        self.click_element(self.quxiaodingdan)

    def click_zaicigoumai(self):
        self.click_element(self.zaicigoumai)

    def element_dingdanzhuangtai_1(self):
        return self.find_element(self.dingdanzhuangtai_1)

    def get_zhinengxiangji_text(self):
        return self.get_element_text(self.zhinengxiangji)
