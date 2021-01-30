import unittest


class LoginCase(unittest.TestCase):
    @unittest.skip("心情不好 跳过")
    def test_01(self):
        print("登录第1条用例")

    def test_02(self):
        print("登录第2条用例")
        self.assertEqual(1, 2, msg="1和2不相等 用例不同过")

    def test_03(self):
        print("登录第3条用例")
        print(aaa)
        self.assertTrue(False)

    def test_04(self):
        print("登录第4条用例")

    def test_05(self):
        print("登录第5条用例")

    def test_06(self):
        print("登录第6条用例")

    def test_07(self):
        print("登录第7条用例")


if __name__ == '__main__':
    unittest.main()
