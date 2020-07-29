
class ConfirmDataImpl(object):
    # 大洲增幅
    @staticmethod
    def continentConfirm():
        from django.db.models import Sum

        from .....models import CountryData
        from .....tools.datetimeSupport import TimeTools
        # 获取时间段
        gapTime = TimeTools.getGapDate()
        # 组成一个dict key为时间 value为一个dict(key为大洲 value为确诊人数)
        ans = {}
        for gdate in gapTime:
            # 查询
            results = CountryData.objects.filter(date=gdate).values("country__continent").annotate(Sum("confirm"))
            results = list(results)
            # print(results)
            tmpDict = {}
            for result in results:
                tmpDict[result["country__continent"]] = result["confirm__sum"]
            ans[gdate.strftime("%Y-%m-%d")] = tmpDict
        # print(ans)
        return ans


    # 人口大国周增幅
    @staticmethod
    def peopleLargeCountryConfirm():

        from .....models import Country
        from .....tools.datetimeSupport import TimeTools
        # 获取时间段
        gapTime = TimeTools.getGapDate()
        # 组成一个dict key为国家 value为一个dict(key为时间 value为确诊人数)
        gapTime = TimeTools.getGapDate(num=6, gapDays=7)
        countryList = ["印度", "俄罗斯", "巴西", "印度尼西亚"]
        ans = {}
        for countryname in countryList:
            country = Country.objects.get(name=countryname)
            dictTmp = {}
            for dategap in gapTime:
                data = country.countrydata_set.filter(date=dategap)
                if len(data) > 0:
                    dictTmp[dategap.strftime("%Y-%m-%d")] = data[0].confirm
                else:
                    dictTmp[dategap.strftime("%Y-%m-%d")] = 0
            ans[countryname] = dictTmp
        return ans


    # 海外总增幅
    @staticmethod
    def overseaConfirm():
        from .....tools.datetimeSupport import TimeTools
        from .....tools.DBOpt import DBTools
        # 获取时间段
        gapTime = TimeTools.getGapDate(num=7, gapDays=7)
        ans = []
        for gdate in gapTime:
            # 查询
            sql = """
            select now.date date,
                round((cast(now.sum as real)-ago.sum)/ago.sum,2) rate,
                now.sum confirm
            from
            (select today.date,sum(today.confirm) sum
                from COVID_19Analyse_countrydata today
                where today.date = date('{}')) now,
            (select sum(lastday.confirm) sum
                from COVID_19Analyse_countrydata lastday
                where lastday.date = (select date('{}','-6 day'))) ago;
            """
            sql = sql.format(gdate.strftime("%Y-%m-%d"), gdate.strftime("%Y-%m-%d"))
            results = DBTools.queryDictList(sql)[0]
            ans.append(results)
        return ans



