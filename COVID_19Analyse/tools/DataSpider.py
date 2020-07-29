# 为web应用提供数据
# 调用下层爬虫/多线程爬虫
# 根据输入，返回有关数据

from .Scrapy.MultiThreadSpider import Crawl
from .datetimeSupport import TimeTools


class DataSpider(object):
    __spider = Crawl()

    # 功能：查询给定国家，给定日期内的疫情数据
    # input:国家名称 开始时间 技术时间
    # output:爬虫查询到的数据信息 一个dict list
    def getDataByDateList(self, country, agodate):
        # 获取时间
        dateList = TimeTools.getGapTime(agodate)
        # 返回答案
        spiderAns = self.__spider.getCountryDatabyDate(country, dateList)
        return spiderAns

    # 获取国家详细信息
    def getCountryDetails(self, country):
        spiderAns = self.__spider.getCountryDetails(country)
        return spiderAns

    # 获取国际疫情信息
    def getInternation_List(self):
        spiderAns = self.__spider.getInternation_List()
        return spiderAns

    # 获取国家列表
    def getCountryList(self):
        spiderAns = self.__spider.getCountry_List()
        return spiderAns

    # 功能：更新信息
    # input：国家：日期的一个dict的list
    # output：更新的数据 dict list
    def update(self, countryDateDictList):
        from .datetimeSupport import TimeTools

        dictlist = []
        for country in countryDateDictList:
            dictTmp = {}
            for key in country:
                countryName = key
                lastFresh = country[key]
            dateList = TimeTools.getGapTime(lastFresh)
            if len(dateList) < 1:
                continue
            # print(dateList)
            dictTmp["country"] = countryName
            dictTmp["dateList"] = dateList
            dictlist.append(dictTmp)
        return self.__spider.update(dictlist)
    # crawl功能
    # 多线程：
    # 1 更新全部
    # def update(self, dictlist):
    # 2 爬取全部
    # def getAll(self, country, dateList):
    # 单线程：
    # 1 获取单个国家详细信息
    # def getCountryDetails(self, country):
    # 2 获取国家列表
    # def getCountry_List(self):
    # 3 获取国际情况
    # def getInternation_List(self):
    # 4 获取国家一段时间疫情数据
    # def getInternation_List(self):
