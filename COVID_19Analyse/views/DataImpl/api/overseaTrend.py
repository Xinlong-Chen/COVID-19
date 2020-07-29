# 新增确诊，确诊，治愈率，病死率

def getOverseaTrend(request):
    from django.http import JsonResponse
    from django.shortcuts import render

    if request.method == "POST":
        from .data.TrendDataImpl import TrendDataImpl
        results = TrendDataImpl.getOverseaTrend()
        return JsonResponse(results, safe=False)
    else:
        return render(request, "COVID_19Analyse/test.html")
