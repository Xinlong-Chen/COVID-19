class SumDataImpl(object):
    # 获取今日情况
    @staticmethod
    def getSummarize():
        from .....tools.Scrapy.MultiThreadSpider import Crawl

        crawl = Crawl()
        ans = crawl.getInternation_List()

        """
        nowConfirm(Compare) 现有确诊(较昨日变化)
        confirm(Compare) 累计确诊(较昨日变化)
        heal(Compare) 累计治愈(较昨日变化)
        dead(Compare) 累计思维(较昨日变化)
        """
        tmp = {'confirm': 0, 'dead': 0, 'heal': 0, 'nowConfirm': 0,
               'confirmCompare': 0, 'nowConfirmCompare': 0,
               'healCompare': 0, 'deadCompare': 0}
        for ansTmp in ans:
            for key in tmp:
                tmp[key] += int(ansTmp[key])
        return tmp

    @staticmethod
    def getCountrySum(country):
        from .....tools.Scrapy.MultiThreadSpider import Crawl

        crawl = Crawl()
        ans = crawl.getInternation_List()

        """
        nowConfirm(Compare) 现有确诊(较昨日变化)
        confirm(Compare) 累计确诊(较昨日变化)
        heal(Compare) 累计治愈(较昨日变化)
        dead(Compare) 累计思维(较昨日变化)
        """
        tmp = {'confirm': 0, 'dead': 0, 'heal': 0, 'nowConfirm': 0,
               'confirmCompare': 0, 'nowConfirmCompare': 0,
               'healCompare': 0, 'deadCompare': 0}
        for ansTmp in ans:
            if ansTmp['name']==country:
                for key in tmp:
                    tmp[key] += int(ansTmp[key])
        return tmp
