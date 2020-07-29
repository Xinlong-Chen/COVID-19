from django.contrib.auth.decorators import login_required


# 大洲增幅
def continentConfirm(request):
    from django.http import JsonResponse, HttpResponse

    if request.method == "POST":
        from .data.ConfirmDataImpl import ConfirmDataImpl
        ans = ConfirmDataImpl.continentConfirm()
        return JsonResponse(ans)
    else:
        return HttpResponse("你所访问的页面不存在", status=404)

@login_required
# 人口大国周增幅
def peopleLargeCountryConfirm(request):
    from django.http import JsonResponse, HttpResponse

    if request.method == "POST":
        from .data.ConfirmDataImpl import ConfirmDataImpl
        ans = ConfirmDataImpl.peopleLargeCountryConfirm()
        return JsonResponse(ans)
    else:
        return HttpResponse("你所访问的页面不存在", status=404)

@login_required
# 海外总增幅
def overseaConfirm(request):
    from django.http import JsonResponse, HttpResponse

    if request.method == "POST":
        from .data.ConfirmDataImpl import ConfirmDataImpl
        ans = ConfirmDataImpl.overseaConfirm()
        return JsonResponse(ans, safe=False)
    else:
        return HttpResponse("你所访问的页面不存在", status=404)
