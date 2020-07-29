# 获取某个国家详细信息
# post country
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required
def getCountryDetails(request):
    from django.http import JsonResponse, HttpResponse

    if request.method == "GET":
        from .data.DetailsDataImpl import DetailsDataImpl
        try:
            country = request.GET.get("country")
        except Exception as e:
            print(str(e))
            return HttpResponse("你所访问的页面不存在", status=404)
        try:
            dict = DetailsDataImpl.getCountryDetails(country)
        except Exception as e:
            print(str(e))
            return HttpResponse("你所访问的页面不存在", status=404)
        return JsonResponse(dict, safe=False)
    else:
        return HttpResponse("你所访问的页面不存在", status=404)

@login_required
def getSumDetails(request):
    from django.http import JsonResponse, HttpResponse

    if request.method == "GET":
        from .data.SumDataImpl import SumDataImpl
        try:
            country = request.GET.get("country")
        except Exception as e:
            print(str(e))
            return HttpResponse("你所访问的页面不存在", status=404)
        dict = SumDataImpl.getCountrySum(country)
        return JsonResponse(dict, safe=False)
    else:
        return HttpResponse("你所访问的页面不存在", status=404)

def getMainCountryDetails(request):
    from django.http import JsonResponse, HttpResponse

    if request.method == "POST":
        from .data.DetailsDataImpl import DetailsDataImpl

        ans = DetailsDataImpl.getMainCountryDetails()
        return JsonResponse(ans)
    else:
        return HttpResponse("你所访问的页面不存在", status=404)
