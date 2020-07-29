# 时间工具

class TimeTools():
    # 根据开始日期、结束日期返回这段时间里所有天(date对象)的集合
    @staticmethod
    def getDatesByTimes(datestart, dateend):
        import datetime
        list = []
        while datestart < dateend:
            datestart += datetime.timedelta(days=1)
            list.append(datestart)
        return list

    # 是否是小时间（1点前数据未更新）
    @staticmethod
    def smallTime():
        import datetime
        nowTime = datetime.datetime.now()
        if nowTime.hour < 1:
            return True
        return False

    # 直接根据起始时间计算
    @staticmethod
    def getGapTime(dateStrat):
        import datetime
        dateEnd = datetime.datetime.today()
        if TimeTools.smallTime():
            dateEnd -= datetime.timedelta(days=1)
        # 要转换一下，不然出错
        dateEnd = dateEnd.date()
        return TimeTools.getDatesByTimes(dateStrat, dateEnd)

    @staticmethod
    def getGapDate(num=15, gapDays=7):
        import datetime
        dateEnd = TimeTools.getToday()
        list = [dateEnd]
        for i in range(num):
            dateEnd -= datetime.timedelta(days=gapDays)
            list.append(dateEnd)
        return list

    @staticmethod
    def getToday():
        import datetime
        if TimeTools.smallTime():
            return datetime.datetime.today().date() - datetime.timedelta(days=1)
        return datetime.datetime.today().date()

    @staticmethod
    def getBegin():
        import datetime
        return datetime.datetime.strptime('2020.01.20', "%Y.%m.%d").date()

    @staticmethod
    def getYesterday():
        import datetime
        if TimeTools.smallTime():
            return datetime.datetime.today().date() - datetime.timedelta(days=2)
        return (datetime.datetime.today()- datetime.timedelta(days=1)).date()

    @staticmethod
    def getLastDay():
        import datetime
        if TimeTools.smallTime():
            return datetime.datetime.today().date() - datetime.timedelta(days=3)
        return (datetime.datetime.today() - datetime.timedelta(days=2)).date()
