# 给web应用提供Excel数据
# 脱机操作
# 读取自己数据库中的数据，然后给用户下载

class ExcelSpool(object):
    from .Scrapy.RW import ExcelData
    excel = ExcelData()

    # 将一个modelList写入excel
    # input：文件路径 模型列表
    # output：一个filepath的excel文件
    def modellist2excel(self, filepath, sheetname, modelList):
        from .ModleOpt import ModelTools
        listList = ModelTools.ModleList2TwoDList(modelList)
        self.twoDList2excel(filepath, sheetname, listList)
        return True

    # 将一个2维列表写入excel
    # input:2维列表
    # output:一个filepath的excel文件
    def twoDList2excel(self, filepath, sheetname, listList):
        from .Scrapy.RW import ExcelData
        excel = ExcelData()
        excel.write(filepath, sheetname, listList)
        return True

    # 将一个dict List写入excel
    # input:dict list
    # output:一个filepath的excel文件
    def dictlist2excel(self, filepath, sheetname, dictList):
        from .ModleOpt import ModelTools
        listList = ModelTools.dictList2TwoDList(dictList)
        self.twoDList2excel(filepath, sheetname, listList)
        return True

    # 将一个dict(dict List)写入excel
    # input:dict(dict List)
    # output:一个filepath的excel文件
    def dictdictlist2excel(self, filepath, dictdictList):
        from .Scrapy.RW import ExcelData
        excel = ExcelData()
        try:
            excel.writeDict_DictList(filepath, dictdictList)
        except Exception as e:
            print(str(e))
        return True

    # 将一个dict(List List)写入excel
    # input:dict(List List)
    # output:一个filepath的excel文件
    def dict_2DList2excel(self,filepath,dict_2DList):
        from .Scrapy.RW import ExcelData
        excel = ExcelData()
        try:
            excel.writeDict_2DList(filepath, dict_2DList)
        except Exception as e:
            print(str(e))
        return True
