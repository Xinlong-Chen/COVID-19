import abc
import datetime
import json
import random
import sys

import requests


class AbcSpider(object):
    @abc.abstractmethod
    # 功能：获取国家详细信息
    # input：国家名称
    # output：指定国家的详细信息 dict list
    def getCountryDetails(self, country):
        pass

    @abc.abstractmethod
    # 功能：获取某国家一段时间内的疫情数据
    # input：国家名，时间（date对象）列表
    # output：一个列表，列表中元素为一个字典，表示一条记录 dict list
    def getCountryDatabyDate(self, country, dateList):
        pass

    @abc.abstractmethod
    # 功能：获取国家列表
    # input：无
    # output：国家列表（名称，所在大洲） dict list
    def getCountry_List(self):
        pass

    @abc.abstractmethod
    # 功能：获取当日国际情况
    # input：无
    # output：当日的国际数据（各国情况） dict list
    def getInternation_List(self):
        pass

    # TODO：国内数据收集


class Spider(AbcSpider):
    __proxypool_url = 'http://127.0.0.1:5555/random'
    __user_agent = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) "
        "Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 "
        "Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR "
        "3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 "
        "Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; "
        ".NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, "
        "like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) "
        "Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) "
        "Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, "
        "like Gecko) Version/4.0 Mobile Safari/533.1",
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) "
        "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) "
        "Version/4.0 Safari/534.13",
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) "
        "Version/6.0.0.337 Mobile Safari/534.1+",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) "
        "wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) "
        "AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        "Openwave/ UCWEB7.0.2.37/28/999",
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
        "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 "
        "Mobile/10A5376e Safari/8536.25",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/79.0.3945.130 Safari/537.36 ",
        "Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile "
        "Safari/10600.6.3 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
        "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
    ]

    def get_random_proxy(self):
        """
        get random proxy from proxypool
        :return: proxy
        """
        return requests.get(self.__proxypool_url).text.strip()

    # 功能：获取指定url内容
    # input：url字符串
    # output：对应url的状态码，内容
    def __getURLContent(self, url):
        proxy = self.get_random_proxy()
        # print('get random proxy', proxy)
        proxies = {'http': 'http://' + proxy}
        header = {'User-Agent': random.choice(self.__user_agent)}
        response = requests.post(url, headers=header, proxies=proxies)
        if response.status_code == 200:
            return response.status_code, response
        else:
            print("not use proxies,use self ip")
            response = requests.post(url, headers=header)
            return response.status_code, response

    # 功能：获取指定国家疫情数据
    # input：国家名
    # output：疫情数据
    # test:ok
    def __getCountryDataJSON(self, country):
        # print("开始爬取 %s 的疫情数据... ... " % country)
        url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%s' % country
        status_code, data = self.__getURLContent(url)
        if status_code != 200:
            print("%s数据爬取失败,状态码%d" % (country, status_code))
            sys.exit()
        data = data.json()["data"]
        if data == None:
            print("%s数据爬取数据为空" % country)
            return
        return data

    # 功能：获取国家详细信息
    # input：国家名称
    # output：指定国家的详细信息 dict list
    # test:ok
    def getCountryDetails(self, country):
        # 得到一个字典
        data = self.__getCountryDataJSON(country)
        if data == None:
            return
        # 标题
        title = []
        for i, str_col in enumerate(['date', 'confirm_add', 'confirm', 'heal', 'dead']):
            title.append(str_col)
        values = [title]
        # 写入内容
        for data_i in data:
            tmp = []
            tmp.append(datetime.datetime.strptime('2020.' + data_i['date'], "%Y.%m.%d").strftime("%Y/%m/%d"))
            tmp.append(data_i['confirm_add'])
            tmp.append(data_i['confirm'])
            tmp.append(data_i['heal'])
            tmp.append(data_i['dead'])
            values.append(tmp)
        print("%s 疫情数据爬取成功！" % country)
        return self.__twoDlist2Dict(values)

    # 功能：获取某国家一段时间内的疫情数据
    # input：国家名，时间（date对象）列表
    # output：一个列表，列表中元素为一个字典，表示一条记录 dict list
    # test:ok
    def getCountryDatabyDate(self, country, dateList):
        data = self.__getCountryDataJSON(country)
        if data == None:
            return
        values = []
        for data_i in data:
            tmpdate = datetime.datetime.strptime('2020.' + data_i['date'], "%Y.%m.%d").date()
            # print(tmpdate)
            if tmpdate in dateList:
                tmp = {}
                tmp["date"] = tmpdate
                tmp["confirm_add"] = data_i['confirm_add']
                tmp["confirm"] = data_i['confirm']
                tmp["heal"] = data_i['heal']
                tmp["dead"] = data_i['dead']
                values.append(tmp)

        # print(values)
        return values

    # 功能：获取国家列表
    # input：无
    # output：国家列表（名称，所在大洲） dict list
    # test:ok
    def getCountry_List(self):
        url = "https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist"

        status_code, data = self.__getURLContent(url)
        if status_code != 200:
            print("数据爬取失败,状态码%d" % (status_code))
            sys.exit()
        data = data.json()["data"]
        if data == None:
            print("数据爬取数据为空")
            return

        # 处理JSON数据
        title = []
        for i, str_col in enumerate(['name', 'continent']):
            title.append(str_col)
        values = [title]
        for children in data:
            tmp = []
            tmp.append(children["name"])
            tmp.append(children["continent"])
            values.append(tmp)
        # 处理为一个二维数组
        return self.__twoDlist2Dict(values)

    # 功能：获取当日国际情况
    # input：无
    # output：当日的国际数据（各国情况） dict list
    # test:ok
    def getInternation_List(self):
        url = "https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist"

        status_code, data = self.__getURLContent(url)
        if status_code != 200:
            print("数据爬取失败,状态码%d" % (status_code))
            sys.exit()
        data = data.json()["data"]
        if data == None:
            print("数据爬取数据为空")
            return

        # 处理JSON数据
        title = []
        for i, str_col in enumerate(['name', 'continent', 'isUpdated',
                                     'confirmAdd', "confirm", "dead", "heal", "nowConfirm",
                                     'confirmCompare', "nowConfirmCompare", "healCompare", "deadCompare"]):
            title.append(str_col)
        values = [title]
        for children in data:
            tmp = []
            tmp.append(children["name"])
            tmp.append(children["continent"])
            tmp.append(children["isUpdated"])
            tmp.append(children["confirmAdd"])
            tmp.append(children["confirm"])
            tmp.append(children["dead"])
            tmp.append(children["heal"])
            tmp.append(children["nowConfirm"])
            tmp.append(children["confirmCompare"])
            tmp.append(children["nowConfirmCompare"])
            tmp.append(children["healCompare"])
            tmp.append(children["deadCompare"])
            values.append(tmp)
        # 处理为一个二维数组
        return self.__twoDlist2Dict(values)

    # 功能：将二维列表转为一个dict list，第一列为label
    # input:二维列表
    # output：dict list
    def __twoDlist2Dict(self, values):
        title = values[0]
        ans = []
        for i in range(1, len(values)):
            tmp = {}
            for j in range(0, len(values[i])):
                tmp[title[j]] = values[i][j]
            ans.append(tmp)
        return ans
