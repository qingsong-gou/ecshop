"""
所有的测试用例类 必须继承 TestCase

setUpClass,tearDownClass,setUp,tearDown 这四个特殊方法 可写可不写,根据实际要求
用例必须以 test开头,且必须要写

每一条用例都需要断言
"""
import unittest


class LoginCase(unittest.TestCase):  # 所有的测试用例类 必须继承 TestCase
    @classmethod
    def setUpClass(cls):
        print("所有的执行前执行!")

    @classmethod
    def tearDownClass(cls):
        print("所有的执行后执行!")

    def setUp(self):
        print("每一个用例执行前执行一次!")

    def tearDown(self):
        print("每一个用例执行后执行一次!")

    def test_case_1(self):
        print("第1条用例")
        # 获取了 页面上的 用户名是 : junfu
        text = "junfu"
        # 实际输入的是: junfu
        # if "junfu" == text:
        #     print("通过")
        # else:
        #     print("失败")
        self.assertEqual("junfu", text, msg="页面显示的用户名和实际的输入的不一致!")

    def test_case_2(self):
        print("第2条用例")
        # 获取了 页面上的 用户名是 : junfu
        text = "junfu"
        # 实际输入的是: jun_fu
        # if "jun_fu" == text:
        #     print("通过")
        # else:
        #     print("失败")
        self.assertEqual("jun_fu", text, msg="页面显示的用户名和实际的输入的不一致!")

    def test_case_3(self):
        self.assertIn("a", ["a", "b"], msg="不存在")


if __name__ == '__main__':
    unittest.main()  # 将当前文件中的所有的用例添加到套件中 并且运行
