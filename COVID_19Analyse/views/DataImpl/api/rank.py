# 病死率排行
# 前端需要传一个flag来：
# flag=1 高->低
# flag=0 低->高
from django.contrib.auth.decorators import login_required


@login_required
def getDeadRank(request):
    from django.http import JsonResponse, HttpResponse
    from django.shortcuts import render

    if request.method == "POST":
        from .data.RankDataImpl import RankDataImpl

        try:
            flag = request.POST.get("flag")
        except:
            return HttpResponse("你所访问的页面不存在", status=404)
        print(flag)

        results= RankDataImpl.getDeadRank(flag)
        if results == False:
            return HttpResponse("你所访问的页面不存在", status=404)
        return JsonResponse(results, safe=False)
    else:
        return render(request, "COVID_19Analyse/test.html")


# 治愈率排行
# 前端需要传一个flag来：
# flag=1 高->低
# flag=0 低->高
@login_required
def getHealRank(request):
    from django.http import JsonResponse, HttpResponse
    from django.shortcuts import render

    if request.method == "POST":
        from .data.RankDataImpl import RankDataImpl
        try:
            flag = request.POST.get("flag")
        except:
            return HttpResponse("你所访问的页面不存在", status=404)
        results = RankDataImpl.getHealRank(flag)
        if results==False:
            return HttpResponse("你所访问的页面不存在", status=404)
        return JsonResponse(results, safe=False)
    else:
        return render(request, "COVID_19Analyse/test.html")


# 最近增长幅度最大的国家
@login_required
def getconfirmAmpl(request):
    from django.http import JsonResponse
    from django.shortcuts import render

    if request.method == "POST":
        from .data.RankDataImpl import RankDataImpl
        results = RankDataImpl.getconfirmAmpl()
        return JsonResponse(results, safe=False)
    else:
        return render(request, "COVID_19Analyse/test.html")

@login_required
def getConfirmRank(request):
    from django.http import JsonResponse
    from django.shortcuts import render
    if request.method == "POST":
        from .data.RankDataImpl import RankDataImpl
        results = RankDataImpl.getConfirmRank()
        return JsonResponse(results, safe=False)
    else:
        return render(request, "COVID_19Analyse/test.html")