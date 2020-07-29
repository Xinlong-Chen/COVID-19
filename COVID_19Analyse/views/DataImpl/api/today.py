# 获取今日情况
from django.contrib.auth.decorators import login_required


@login_required
def getToday(request):
    from django.http import JsonResponse, HttpResponse

    if request.method == "POST":
        from .data.TodayDataImpl import TodayDataImpl

        ans = TodayDataImpl.getToday()
        return JsonResponse(ans, safe=False)
    else:
        return HttpResponse("你所访问的页面不存在", status=404)

