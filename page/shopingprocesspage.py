from common.base import Base


class ShoppingProcessPage(Base):
    submitaddress1 = ("css selector", "#theForm > div > table > tbody > tr:nth-child(5) > td > input.bnt_blue_2")  # 定位配送至这个地址按钮
    shopprice = (
        "css selector", "#theForm > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(4)")  # 定位本店价格
    updategoodslist = ("css selector", "#theForm > div:nth-child(2) > h6 > a")  # 定位修改商品列表
    updateconsigneeinfo = ("css selector", "#theForm > div:nth-child(4) > h6 > a")  # 定位修改收货人信息
    submitaddress2 = ("css selector", "#theForm > div > table > tbody > tr:nth-child(5) > td > input.bnt_blue_2")
    STO = ("css selector", "input[type='radio'][value='5']")  # 定位申通快递
    EMS = ("css selector", "input[type='radio'][value='6']")  # 定位邮局平邮
    STOCost = ("css selector", "#shippingTable > tbody > tr:nth-child(2) > td:nth-child(4)")  # 定位申通快递费用
    EMSCost = ("css selector", "#shippingTable > tbody > tr:nth-child(3) > td:nth-child(4)")  # 定位邮政快递费用
    CourierCost = (
        "css selector", "#ECS_ORDERTOTAL > table > tbody > tr:nth-child(2) > td > font:nth-child(2)")  # 定位订单配送费用
    CommitOrder = (
        "css selector", "#theForm > div:nth-child(16) > div:nth-child(3) > input[type=image]:nth-child(1)")  # 定位提交订单
    Notice = ("css selector", "body > div:nth-child(7) > div > h6")  # 定位提交订单后的提示信息
    Noticeexpress=("css selector","body > div:nth-child(7) > div > table > tbody > tr:nth-child(1) > td > strong:nth-child(1)") #定位快递提示信息
    usercenter = ("link text", "用户中心")  # 定位用户中心
    backhomepage = ("link text", "返回首页")  # 定位返回首页
    balancepayment=("css selector","input[name='payment'][value='1']")
    cardpayment=("css selector","input[name='payment'][value='2']")

    def clicksubmit(self):
        """
        点击配送至这个地址
        :return:
        """
        self.click_element(self.submitaddress1,timeout=30)

    def getpricetext(self):
        """
        获取本店价格
        :return:
        """
        return self.get_element_text(self.shopprice)

    def clickupdategoodslist(self):
        """
        点击修改商品列表
        :return:
        """
        self.click_element(self.updategoodslist)

    def clickupdateconsigneeinfo(self):
        """
        点击修改收货人信息
        :return:
        """
        self.click_element(self.updateconsigneeinfo)

    def findsubmitaddress2(self):
        """
        查找页面是否存在配送至这个地址的元素,存在返回true,不存在返回false
        :return:
        """
        try:
            self.find_element(self.submitaddress2)
            return True
        except Exception:
            return False

    def clickSTO(self):
        """
        点击选择申通
        :return:
        """
        self.click_element(self.STO,timeout=30)

    def clickEMS(self):
        """
        点击选择邮政平邮
        :return:
        """
        self.click_element(self.EMS,timeout=30)

    def getSTOmoney(self):
        """
        获取申通快递的费用
        :return:费用
        """
        return self.get_element_text(self.STOCost)

    def getEMSmoney(self):
        """
        获取邮政快递费用
        :return:费用
        """
        return self.get_element_text(self.EMSCost,timeout=30)

    def getCourierCost(self):
        """
        获取订单的运输费用
        :return: 费用
        """
        return self.get_element_text(self.CourierCost)

    def clickcommitorder(self):
        """
        点击提交订单
        :return:
        """
        self.click_element(self.CommitOrder)

    def getnotice(self):
        """
        获取提交订单后的提示信息
        :return: 提示信息
        """
        return self.get_element_text(self.Notice)

    def clickbackhomepage(self):
        """
        点击返回首页
        :return:
        """
        self.click_element(self.backhomepage)

    def clickusercenter(self):
        """
        点击用户中心
        :return:
        """
        self.click_element(self.usercenter)

    def getexpressnotice(self):
        """
        获取提交订单后的提示信息
        :return: 提示信息
        """
        return self.get_element_text(self.Noticeexpress)

    def clickbalancepayment(self):
        self.click_element(self.balancepayment)

    def clickcardpayment(self):
        self.click_element(self.cardpayment)
