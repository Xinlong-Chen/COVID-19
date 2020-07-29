class RankDataImpl(object):
    # 病死率排行
    # 前端需要传一个flag来：
    # flag=1 高->低
    # flag=0 低->高
    @staticmethod
    def getDeadRank(flag):
        from .....tools.DBOpt import DBTools
        if flag not in ("1", "0"):
            return False
        sql = """
        select country.name,round(tmp.d/tmp.c,4) deadrate
        from COVID_19Analyse_country country
            join
            (
                select cast(data.dead as REAL) d,data.confirm c,data.country_id
                from COVID_19Analyse_countrydata data
                where data.date = '2020-06-18' and c >1000
                order by d/c
                {}
                limit 0,10
            ) tmp
        on tmp.country_id=country.id;
        """
        if flag == "1":
            sql = sql.format("desc")
        else:
            sql = sql.format("")
        results = DBTools.queryDictList(sql)
        return results


    # 治愈率排行
    # 前端需要传一个flag来：
    # flag=1 高->低
    # flag=0 低->高
    @staticmethod
    def getHealRank(flag):

        from .....tools.DBOpt import DBTools

        if flag not in ("1", "0"):
            return False
        sql = """
        select country.name,round(tmp.h/tmp.c,4) healrate
        from COVID_19Analyse_country country,
            (
                select cast(heal as REAL) h,confirm c,country_id
                from COVID_19Analyse_countrydata
                where date = '2020-06-18' and c >1000
                order by h/c
                {}
                limit 0,10
            ) tmp
        where tmp.country_id=country.id;
        """
        if flag == "1":
            sql = sql.format("desc")
        else:
            sql = sql.format("")
        results = DBTools.queryDictList(sql)
        return results


    # 最近增长幅度最大的国家
    @staticmethod
    def getconfirmAmpl():
        from .....tools.DBOpt import DBTools
        from .....tools.datetimeSupport import TimeTools
        today = TimeTools.getToday()
        sql = """
        select country.name,confirmAdd
        from COVID_19Analyse_country country
        join
            (
                select now.country_id,((cast(now.confirm as real)-ago.confirm)/ago.confirm) as confirmAdd
                from
                (
                    select today.confirm,country_id
                        from COVID_19Analyse_countrydata today
                        where today.date = '{}'
                          and today.confirm>1000
                ) now
                join
                (
                    select lastday.confirm,lastday.country_id
                        from COVID_19Analyse_countrydata lastday
                        where lastday.date = (select date('{}','-6 day'))

                ) ago
                on now.country_id = ago.country_id
            ) addTmp
        on addTmp.country_id = country.id
        order by addTmp.confirmAdd
        desc
        limit 0,10;
        """
        sql = sql.format(today.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d"))
        results = DBTools.queryDictList(sql)
        return results

    @staticmethod
    def getConfirmRank():
        from .....tools.DBOpt import DBTools
        from .....tools.datetimeSupport import TimeTools
        today = TimeTools.getToday()
        sql = """
        select name,confirm_add from COVID_19Analyse_country country
        join
        (
            select data.confirm_add,data.country_id
            from COVID_19Analyse_countrydata data
            where data.date = '{}'
            order by data.confirm_add
              desc
            limit 0,10
        ) tmp
        on country.id = country_id
        """
        sql = sql.format(today.strftime("%Y-%m-%d"))
        results = DBTools.queryDictList(sql)
        return results

