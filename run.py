import unittest
from datetime import datetime
from common.HTMLTestRunnerPlugins import HTMLTestRunner


# # 添加测试套件 方法一
# from case.test_case_01 import LoginCase
# from case.test_case_02 import ShopCase
# # 实例化测试套件对象
# suite = unittest.TestSuite()
# # 将用例添加到 测试套件的对象中
# suite.addTest(LoginCase('test_01'))
# suite.addTest(ShopCase('test_03'))
# 获取当前时间
time_obj = datetime.now()
time_str = time_obj.strftime("%Y_%m_%d-%H_%M_%S")
def run(pattern, dir="./case"):
    # 实例化测试套件(添加用例 一个步骤)
    loader = unittest.defaultTestLoader.discover(dir, pattern=pattern)

    runner = HTMLTestRunner(
        title="自动化测试报告",
        description="这里是用例执行的描述",
        stream=open(f"{time_str}_测试报告.html", "wb"),
        tester="刘俊甫"
    )
    runner.run(loader)


# run("*case*.opy")
run("login_case_01.py")

# # # 实例化执行对象
# # runner = unittest.TextTestRunner()
# # # 使用执行对象 执行测试套件中的用例
# # runner.run(loader)
#
#
# """
# 测试生成的结果中 :
#     . --> 用例执行通过
#     s --> 用例跳过
#     F --> 用例执行不通过 断言失败(预期结果和实际结果不一致)
#     E --> 用例里面的某个步骤错误了
# """
# """
# 3.使用163邮箱 或者 QQ邮箱发邮件(所有的元素定位使用显等待)
# """
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.wait import WebDriverWait
#
# # 获取个人资料路径
# user_data = r"--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"
# option = webdriver.ChromeOptions()
# option.add_argument(user_data)
#
# driver = webdriver.Chrome(options=option)
# driver.maximize_window()
# driver.get("https://mail.qq.com/")
#
#
# def find_element_css(css, timeout=5):
#     element = WebDriverWait(driver, timeout).until(ec.presence_of_element_located(("css selector", css)))
#     return element
#
#
# # composebtn = ec.presence_of_element_located(("css selector", "a#composebtn"))(driver)
# composebtn = find_element_css("a#composebtn")
# composebtn.click()
#
# driver.switch_to.frame("mainFrame")
#
# # 输入收件人
# find_element_css("input[aria-label='收件人']").send_keys("1341745883@qq.com")
#
# # 主题
# find_element_css("input#subject").send_keys("你好!")
# print(f"{time_str}_测试报告.html")
# # 附件
# find_element_css("span#composecontainer input[name='UploadFile']").send_keys(f"E:/1120软件测试/12_selenium页面自动化测试/2021_01_28_selenium自动化测试day06/code/上课代码/ECshop/{time_str}_测试报告.html")
#
# # 切换iframe
# iframe = find_element_css("iframe.qmEditorIfrmEditArea")
# driver.switch_to.frame(iframe)
#
# # 输入正文
# find_element_css("body").send_keys("123456")
#
# # 跳出iframe
# driver.switch_to.parent_frame()
#
# # 点击发送
# find_element_css("a[name='sendbtn']").click()
#
# driver.quit()

