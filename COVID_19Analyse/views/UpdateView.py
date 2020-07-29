
# 更新整体数据
from django.contrib.auth.decorators import login_required

from COVID_19Analyse.models import CountryData


@login_required
def update(request):
    from django.http import HttpResponse
    from django.shortcuts import render

    from ..models import Country
    from ..tools.DataSpider import DataSpider
    from ..tools.datetimeSupport import TimeTools
    if request.method == "POST":
        print("----------------更新全部数据----------------")
        # 爬取数据
        spider = DataSpider()

        # 获取国家列表
        countryList = spider.getCountryList()
        for country in countryList:
            print(country['name'])
            try:
                Country.objects.get(name=country['name'])
            except Exception as e:
                # 没有该数据,保存之
                countryObject = Country(name=country['name'],continent=country['continent'])
                countryObject.save()


        # 获取国家列表
        countries = Country.objects.all()
        countryDateDictList = []
        # 设置开始时间
        for country in countries:
            dictTmp = {country.name: TimeTools.getBegin()}
            countryDateDictList.append(dictTmp)
        Timelist = TimeTools.getGapTime(TimeTools.getBegin())
        Timedict = {}
        for timeTmp in Timelist:
            Timedict[timeTmp] = 0


        ans = spider.update(countryDateDictList)

        for key in ans:
            print(key)
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
        print("-----------------更新结束-----------------")
        print()

        return HttpResponse("刷新成功", status=200)
    else:
        return render(request, "COVID_19Analyse/update.html")
