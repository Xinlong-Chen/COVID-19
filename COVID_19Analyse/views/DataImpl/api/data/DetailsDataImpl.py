class DetailsDataImpl(object):
    @staticmethod
    # 获取某个国家详细信息
    # post country
    def getCountryDetails(country):
        from .....models import Country

        from .....tools.ModleOpt import ModelTools
        results = (Country.objects.get(name=country).countrydata_set.all().order_by("-date"))[0:125]
        dict = ModelTools.ModleList2DictList(results)
        return dict

    @staticmethod
    def getMainCountryDetails():
        from .....models import Country
        CountryList = ["意大利", "巴西", "西班牙", "德国", "英国", "法国", "美国", "俄罗斯"]
        ans = {}
        for country in CountryList:
            results = (Country.objects.get(name=country).countrydata_set.all().values("date", "confirm").order_by(
                "-date"))[0:115]
            results = list(results)
            ans[country] = results
        return ans