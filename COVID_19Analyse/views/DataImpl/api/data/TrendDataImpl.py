class TrendDataImpl(object):
    @staticmethod
    # 新增确诊，确诊，治愈率，病死率
    def getOverseaTrend():
        from .....tools.DBOpt import DBTools

        sql = """
        select data.date date,sum(data.confirm) confirm,
               sum(data.confirm_add) confirm_add,
               sum(data.confirm)-sum(data.heal)-sum(data.dead) confirm_now,
               cast(sum(data.heal) as real)/sum(data.confirm) healrate,
               cast(sum(data.dead) as real)/sum(data.confirm) deadrate
        from COVID_19Analyse_countrydata data
        group by data.date
        order by date
        desc
        limit 0,120;
        """
        results = DBTools.queryDictList(sql)
        return results
