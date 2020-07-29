# 获取今日情况
def getSummarize(request):
    from django.http import JsonResponse, HttpResponse

    if request.method == "POST":
        from .data.SumDataImpl import SumDataImpl
        tmp = SumDataImpl.getSummarize()
        return JsonResponse(tmp)
    else:
        return HttpResponse("你所访问的页面不存在", status=404)
