class ToExcelData(object):
    from ....tools.ModleOpt import ModelTools

    # return Dict_DictList
    @staticmethod
    def getMainCountryDetails():
        from ...DataImpl.api.data.DetailsDataImpl import DetailsDataImpl
        datas = DetailsDataImpl.getMainCountryDetails()
        return datas


    # return Dict_2DList
    @staticmethod
    def peopleLargeCountryConfirm():
        from ...DataImpl.api.data.ConfirmDataImpl import ConfirmDataImpl
        datas = ConfirmDataImpl.peopleLargeCountryConfirm()
        ansDict = {}
        title = ["date", "confirm"]
        for key in datas:
            ansDict[key] = ToExcelData.__dict2_2DList(datas[key],title)
        return ansDict

    @staticmethod
    def continentConfirm():
        from ...DataImpl.api.data.ConfirmDataImpl import ConfirmDataImpl
        ansDict = {}
        title = ["continent", "confirm"]
        datas = ConfirmDataImpl.continentConfirm()
        for key in datas:
            ansDict[key] = ToExcelData.__dict2_2DList(datas[key],title)
        return ansDict

    @staticmethod
    def getOverseaTrend():
        from ...DataImpl.api.data.TrendDataImpl import TrendDataImpl
        datas = TrendDataImpl.getOverseaTrend()
        return datas

    @staticmethod
    def getRank():
        ansDict = {}
        ansDict["确诊排行"] = ToExcelData.getConfirmRank()
        ansDict["治愈率排行(高->低)"] = ToExcelData.__getHealRank("1")
        ansDict["治愈率排行(低->高)"] = ToExcelData.__getHealRank("0")
        ansDict["病死率排行(高->低)"] = ToExcelData.__getDeadRank("1")
        ansDict["病死率排行(低->高)"] = ToExcelData.__getDeadRank("0")
        return ansDict

    @staticmethod
    def getConfirmRank():
        from ...DataImpl.api.data.RankDataImpl import RankDataImpl
        datas = RankDataImpl.getConfirmRank()
        return datas

    @staticmethod
    def __getHealRank(flag):
        from ...DataImpl.api.data.RankDataImpl import RankDataImpl
        datas = RankDataImpl.getHealRank(flag)
        return datas

    @staticmethod
    def __getDeadRank(flag):
        from ...DataImpl.api.data.RankDataImpl import RankDataImpl
        datas = RankDataImpl.getDeadRank(flag)
        return datas

    @staticmethod
    def __getconfirmAmpl():
        from ...DataImpl.api.data.RankDataImpl import RankDataImpl
        datas = RankDataImpl.getconfirmAmpl()
        return datas

    @staticmethod
    def __dict2_2DList(dict,title):
        ansList = [title]
        for key in dict:
            ansList.append([key, dict[key]])
        return ansList
