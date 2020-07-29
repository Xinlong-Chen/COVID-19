import threading
import time
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED

from .spider import Spider


class Crawl(object):
    __spider = Spider()

    __updateResults = {}
    __updateWritelock = threading.Lock()

    def __addUpdateResults(self, key, result):
        with self.__updateWritelock:
            self.__updateResults[key] = result

    __getResults = {}
    __writelock = threading.Lock()

    def __addGetResults(self, key, result):
        with self.__writelock:
            self.__getResults[key] = result

    # return : dict key国家 value数据
    # 获取一个国家的信息
    def __task1(self, countryName):
        # task
        data = self.__spider.getCountryDetails(countryName)
        self.__addGetResults(countryName, data)
        # print(dict)
        # time.sleep(3)

    def __task2(self, country, dateList):
        data = self.__spider.getCountryDatabyDate(country, dateList)
        self.__addUpdateResults(country, data)

    # 多线程 获取全部数据
    # return : dict key国家 value数据
    def getAll(self):
        try:
            self.__getResults = {}
            countrytmp = self.__spider.getCountry_List()
            countryList = []
            for tmp in countrytmp:
                countryList.append(tmp["name"])
            with ThreadPoolExecutor(max_workers=max(11, len(countryList) // 11)) as t:
                all_task = [t.submit(self.__task1, data) for data in countryList]
                wait(all_task, return_when=FIRST_COMPLETED)
        finally:
            return self.__getResults

    # 多线程 更新数据
    # input:dict list
    # dict key：country ， dateList
    def update(self, dictlist):
        # print(dictlist)
        try:
            self.__updateResults = {}
            with ThreadPoolExecutor(max_workers=11) as t:
                all_task = [t.submit(self.__task2, data["country"], data["dateList"]) for data in dictlist]
                wait(all_task, return_when=FIRST_COMPLETED)
            return self.__updateResults
        finally:
            pass

    # 单线程：
    # 1 获取单个国家详细信息
    # def getCountryDetails(self, country):
    # 2 获取国家列表
    # def getCountry_List(self):
    # 3 获取国际情况
    # def getInternation_List(self):
    # 4 获取国家一段时间疫情数据
    # def getInternation_List(self):
    def getCountryDetails(self, country):
        return self.__spider.getCountryDetails(country)

    def getCountry_List(self):
        return self.__spider.getCountry_List()

    def getInternation_List(self):
        return self.__spider.getInternation_List()

    def getCountryDatabyDate(self, country, dateList):
        return self.__spider.getCountryDatabyDate(country, dateList)
