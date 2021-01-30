"""
所有的测试用例类 必须继承 TestCase

setUpClass,tearDownClass,setUp,tearDown 这四个特殊方法 可写可不写,根据实际要求
用例必须以 test开头,且必须要写

每一条用例都需要断言
"""
import unittest


@unittest.skip("今天心情不好,不想测了")
class LoginCase(unittest.TestCase):  # 所有的测试用例类 必须继承 TestCase
    @unittest.skip("因为功能阻塞")
    def test_case_1(self):
        # 获取了 页面上的 用户名是 : junfu
        text = "junfu"
        # 实际输入的是: junfu
        self.assertEqual("junfu", text, msg="页面显示的用户名和实际的输入的不一致!")

    @unittest.skipIf(2 > 1, "满足条件 跳过测试用例!")  # 满足条件 跳过测试用例
    def test_case_2(self):
        # 获取了 页面上的 用户名是 : junfu
        text = "junfu"
        # 实际输入的是: jun_fu
        self.assertEqual("jun_fu", text, msg="页面显示的用户名和实际的输入的不一致!")

    @unittest.skipUnless(1 > 2, "不满足条件跳过")  # 不满足条件跳过
    def test_case_3(self):
        self.assertIn("a", ["a", "b"], msg="不存在")

    def test_case_4(self):
        self.assertTrue(True, msg="不存在")

    def test_case_5(self):
        self.assertTrue(False, msg="不存在")


if __name__ == '__main__':
    unittest.main()  # 将当前文件中的所有的用例添加到套件中 并且运行
