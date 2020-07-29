from django.forms import model_to_dict


class ModelTools(object):
    @staticmethod
    # 功能：将一个model list，转为dict list
    # input：model list
    # output：dict list
    def ModleList2DictList(modleList):
        ans = []
        for data in modleList:
            tmp = model_to_dict(data)
            try:
                del tmp["id"]
            finally:
                pass
            ans.append(tmp)
        return ans

    # 功能：将一个model list，转为二维列表,第一列为label
    # input：model list
    # output：二维列表
    @staticmethod
    def ModleList2TwoDList(modelList):
        dictList = ModelTools.ModleList2DictList(modelList)
        twoDList = ModelTools.dictList2TwoDList(dictList)
        return twoDList

    # 功能：将一个dict list，转为二维列表,第一列为label
    # input：dict list
    # output：二维列表
    @staticmethod
    def dictList2TwoDList(dictList):
        if len(dictList) < 1:
            return []
        title = []
        for key in dictList[0]:
            title.append(key)
        ans = [title]
        for dictTmp in dictList:
            Listtmp = []
            for key in dictTmp:
                Listtmp.append(dictTmp[key])
            ans.append(Listtmp)
        return ans

    # 功能：将二维列表转为一个dict list，第一列为label
    # input:二维列表
    # output：dict list
    @staticmethod
    def twoDlist2DictList(values):
        title = values[0]
        ans = []
        for i in range(1, len(values)):
            tmp = {}
            for j in range(0, len(values[i])):
                tmp[title[j]] = values[i][j]
            ans.append(tmp)
        return ans


