import pandas


class OpenExcel(object):
    def __init__(self, fileName, converters):
        self.excel = pandas.read_excel(fileName, converters=converters)

    def read_dict(self):
        """
        列表套字典
        :return:
        """
        li = []
        for i in self.excel.index.values:
            li.append(self.excel.loc[i].to_dict())
        return li

    def read_list(self):
        return self.excel.values.tolist()


if __name__ == '__main__':
    oe = OpenExcel('测试数据.xlsx', {"password": str, "number": str})
    print(oe.read_dict())

    print(oe.read_list())
