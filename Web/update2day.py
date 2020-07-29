
def hourUpdate():
    import datetime
    from COVID_19Analyse.models import Country, CountryData

    from COVID_19Analyse.tools.datetimeSupport import TimeTools
    from COVID_19Analyse.tools.DataSpider import DataSpider

    print("----------------更新全部数据----------------")

    print(datetime.datetime.today().strftime("%Y-%m-%d %H:%M"))
    # 爬取数据
    spider = DataSpider()

    # 获取国家列表
    countryList = spider.getCountryList()
    for country in countryList:
        try:
            Country.objects.get(name=country['name'])
        except Exception as e:
            # 没有该数据,保存之
            countryObject = Country(name=country['name'], continent=country['continent'])
            countryObject.save()

    # 获取国家列表
    countries = Country.objects.all()
    countryDateDictList = []
    # 设置开始时间
    for country in countries:
        # 开始时间为前天
        dictTmp = {country.name: TimeTools.getLastDay()}
        countryDateDictList.append(dictTmp)
    Timelist = TimeTools.getGapTime(TimeTools.getLastDay())
    Timedict = {}
    for timeTmp in Timelist:
        Timedict[timeTmp] = 0

    ans = spider.update(countryDateDictList)

    for key in ans:
        countryObject = Country.objects.get(name=key)
        for data in ans[key]:
            try:
                dataObject = countryObject.countrydata_set.get(date=data["date"])
            except Exception as e:
                dataObject = CountryData(date=data["date"], country=countryObject)
            Timedict[data["date"]] += 1
            dataObject.confirm_add = data["confirm_add"]
            dataObject.confirm = data["confirm"]
            dataObject.heal = data["heal"]
            dataObject.dead = data["dead"]

            dataObject.save()
    for timeTmp in Timedict:
        print("{:<12} {}条数据已更新".format(timeTmp.strftime("%Y-%m-%d"), Timedict[timeTmp]))
    rebulid()
    print("文件目录已更新")
    print("-----------------更新结束-----------------")
    print()


def rebulid():
    import shutil,os
    path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
    path+="/COVID_19Analyse/static/COVID_19Analyse/Upload/"
    shutil.rmtree(path)
    os.mkdir(path)
    os.mkdir(path+'country/')
