class DBTools(object):
    @staticmethod
    def queryDictList(sql):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(sql)
        title = []
        for field in cursor.description:
            title.append(field[0])
        ans = []
        for row in cursor.fetchall():
            dictTmp = {}
            for i in range(len(title)):
                dictTmp[title[i]] = row[i]
            ans.append(dictTmp)
        return ans

    @staticmethod
    def queryList(sql):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(sql)
        title = []
        for field in cursor.description:
            title.append(field[0])
        ans = [title]
        for row in cursor.fetchall():
            ans.append(list(row))
        return ans
