from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# 需要提供一个参数type
# 下载功能

# 屏蔽掉csrf
@csrf_exempt
@login_required
def download_file(request):
    import os

    from django.http import HttpResponse, FileResponse
    from django.shortcuts import render

    if request.method == "GET":
        return render(request, "COVID_19Analyse/filedown.html")

    # 获取操作类型
    try:
        type = request.POST.get("datatype")
    except Exception as e:
        return HttpResponse("你所访问的页面不存在", status=404)

    if type=="details":
        try:
            country = request.POST.get("country")

        except Exception as e:
            return HttpResponse("你所访问的页面不存在", status=404)
    else:
        country=""

    path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")


    the_file_name = getFileName(type,country)
    if the_file_name==False:
        return HttpResponse("你所访问的页面不存在", status=404)
    # 文件名 存储路径
    if type=="details":
        filename = path + '/static/COVID_19Analyse/Upload/country/' + the_file_name
    else:
        filename = path + '/static/COVID_19Analyse/Upload/' + the_file_name

    if judge_exit(filename)==False:
        # 不存在该文件
        # 获取数据
        createFile(filename,type,country)
    # 发送文件
    file = open(filename, "rb")
    response = FileResponse(file)
    response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response['Content-Disposition'] = 'attachment; ' \
                                      'filename=' + the_file_name.encode('utf-8').decode('ISO-8859-1')

    return response


def judge_exit(file_path):
    import os
    if(os.path.exists(file_path)):
        return True
    return False

def getFileName(type,country=""):
    if type == "maincountry":
        the_file_name = "主要国家.xlsx"
    elif type == "plc":
        the_file_name = "人口大国.xlsx"
    elif type == "continent":
        the_file_name = "大洲情况.xlsx"
        pass
    elif type == "trend":
        the_file_name = "全球趋势.xlsx"
    elif type == "rank":
        the_file_name = "全球榜单.xlsx"
    elif type == "details":
        the_file_name = country+".xlsx"
    else:
        return False
    return the_file_name

def createFile(filename,type,country=""):
    from ...tools.ExcelOpt import ExcelSpool
    from .data.ToExcelData import ToExcelData

    excel = ExcelSpool()

    if type == "maincountry":
        results = ToExcelData.getMainCountryDetails()
        excel.dictdictlist2excel(filename, results)
    elif type == "plc":
        results = ToExcelData.peopleLargeCountryConfirm()
        excel.dict_2DList2excel(filename, results)
    elif type == "continent":
        results = ToExcelData.continentConfirm()
        excel.dict_2DList2excel(filename, results)
        pass
    elif type == "trend":
        results = ToExcelData.getOverseaTrend()
        excel.dictlist2excel(filename, "海外疫情数据", results)
    elif type == "rank":
        results = ToExcelData.getRank()
        excel.dictdictlist2excel(filename, results)
    elif type == "details":
        from ...models import Country
        try:
            countryDataModels = (Country.objects.get(name=country).countrydata_set.all().order_by("-date"))
            excel.modellist2excel(filename, country, countryDataModels)
        except Exception as e:
            print(str(e))
            return False

