from common.base import Base


class ShoppingCartPage(Base):
    number = ("css selector", "input[class='inputBg'][size='4']")  # 定位数量输入框
    update = ("name", "submit")  # 定位更新购物车
    reset = ("css selector", "input[value='清空购物车']")  # 定位清空购物车
    delete = ("link text", "删除")  # 定位删除
    notice = ("css selector", "div[align='center'] p")
    logout = ("link text", "退出")  # 定位退出
    shoppingcart = ("link text", "购物车(0)")  # 定位购物车
    camera = ("link text", "智能相机")  # 定位智能相机
    collet = ("link text", "放入收藏夹")  # 定位放入收藏夹
    usercenter = ("link text", "用户中心")  # 定位用户中心
    gocheckout = ("css selector", "img[src='themes/default/images/checkout.gif']")  # 定位去结算
    shopprice = ("css selector", "#formCart > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)")  # 定位本店价格

    def sendkeysnumber(self, number):
        """
        输入商品数量，先清空里面的，再输入新的
        :param number:商品数量
        :return:
        """
        self.clearnumber(self.number)
        self.sendKeysElement(self.number, number)

    def clickupdate(self):
        """
        点击更新按钮
        :return:
        """
        self.clickElement(self.update)

    def clickshoppingcart(self):
        """
        点击购物车链接
        :return:
        """
        self.clickElement(self.shoppingcart)

    def cleargoods(self):
        """
        点击清空购物车按钮
        :return:
        """
        self.clickElement(self.reset)

    def clickdelete(self):
        """
        点击删除按钮
        :return:
        """
        self.clickElement(self.delete)

    def numbervalue(self, text):
        """
        判断输入框内的值是否为指定值
        :param text: 指定的值
        :return: 如果是返回true，如果不是返回false
        """
        res = self.value(self.number, text)
        return res

    def noticetext(self, text):
        """
        判断元素中的内容是否为指定内容
        :param text: 指定的内容
        :return: 如果是就返回内容，如果不是返回false
        """
        try:
            n = self.text(self.notice, text)
            return n
        except Exception:
            return False

    def clicklogout(self):
        """
        点击退出链接
        :return:
        """
        self.clickElement(self.logout)

    def findcamera(self):
        """
        判断照相机是否存在页面
        :return:如果存在返回元素，不存在就返回False
        """
        try:
            return self.element(self.camera)
        except Exception:
            return False

    def findupdate(self):
        """
        判断更新购物车按钮是否存在页面
        :return: 存在返回true，不存在返回false
        """
        try:
            return self.element(self.update)
        except Exception:
            return False

    def clickcollect(self):
        """
        点击放入收藏夹
        :return:
        """
        self.clickElement(self.collet)

    def clickusercenter(self):
        """
        点击用户中心,进入用户中心页面
        :return:
        """
        self.clickElement(self.usercenter)

    def clickgocheckout(self):
        self.clickElement(self.gocheckout)

    def getpricetext(self):
        return self.getElementText(self.shopprice, timeout=20)
