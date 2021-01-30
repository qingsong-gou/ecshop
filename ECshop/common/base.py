"""
对于 selenium的二次封装
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def open_browser(type='谷歌'):
    if type == "谷歌":
        driver = webdriver.Chrome()
    elif type == "火狐":
        driver = webdriver.Firefox()
    elif type == "Ie":
        driver = webdriver.Ie()
    else:
        raise TypeError("浏览的类型错误:谷歌 火狐 Ie")
    driver.maximize_window()
    return driver


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        """
        进入指定的url页面
        :param url: 网址
        :return:
        """
        self.driver.get(url)

    def find_element(self, locater, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locater))
        return element

    def click_element(self, locater, timeout=5):
        # 定位
        element = self.find_element(locater, timeout)
        # 点击
        element.click()

    def send_keys_element(self, locater, text, timeout=5):
        # 定位
        element = self.find_element(locater, timeout)
        # 点击
        element.send_keys(text)

    def get_element_text(self, locater, timeout=5):
        # 定位
        element = self.find_element(locater, timeout)
        # 获取
        return element.text

    def quit(self):
        self.driver.quit()

# if __name__ == '__main__':
#     driver = open_browser()
#     print(driver)
