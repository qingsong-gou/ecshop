from common.base import Base
from selenium.webdriver.common.by import By


class CoolectionPage(Base):
    homePage_loc = (By.LINK_TEXT, "首页")
    camera_loc = (By.CSS_SELECTOR, "a[href = 'goods.php?id=72']")
    local_price = (By.CSS_SELECTOR, "#ECS_SHOPPRICE")
    button = (By.CSS_SELECTOR, "[href='javascript:collect(72)']")
    usercenter_loc = (By.LINK_TEXT, "用户中心")
    user_collect_loc = (By.CSS_SELECTOR, "[href='user.php?act=collection_list']")
    my_button = (By.CSS_SELECTOR, "span.goods-price")

    def click_homPage(self):
        self.click_element(self.homePage_loc)

    def click_camera_loc(self):
        self.click_element(self.camera_loc)

    def get_local_price(self):
        return self.get_element_text(self.local_price)

    def click_button(self):
        self.click_element(self.button)

    def click_alert(self):
        return self.driver.switch_to.alert

    def accept_alert(self):
        self.click_alert().accept()

    def usercenter_click(self):
        self.click_element(self.usercenter_loc)

    def user_collect_loc_click(self):
        self.click_element(self.user_collect_loc)

    def get_local_price2(self):
        return self.get_element_text(self.my_button)
