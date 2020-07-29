class TodayDataImpl(object):
    # 获取今日情况
    @staticmethod
    def getToday():
        from .....models import Country

        from .....tools.DataSpider import DataSpider

        spider = DataSpider()
        ans = spider.getInternation_List()
        ans.sort(key=lambda ee: ee["confirm"], reverse=True)
        countryTmp = Country.objects.all()
        countryList = []
        for country in countryTmp:
            countryList.append(country.name)
        keyList = ["name","continent","confirmAdd","confirm","heal","dead"]
        for i in range(len(ans)):
            ans[i] = TodayDataImpl.__delDict(ans[i],keyList)
            if ans[i]["name"] in countryList:
                ans[i]["details"] = True
            else:
                ans[i]["details"] = False
        return ans

    @staticmethod
    def __delDict(dict,keyList):
        keyTmp = []
        for key in dict:
            keyTmp.append(key)
        for key in keyTmp:
            if key not in keyList:
                try:
                    del dict[key]
                except:
                    pass
        return dict