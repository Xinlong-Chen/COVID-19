from django.shortcuts import render,redirect
from django.http import JsonResponse

from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, "login/register.html")
    else:
        try:
            email = request.POST.get("InputEmail").strip()
        except Exception as e:
            dict = {"err": "email输入错误！"}
            return JsonResponse(dict)
        try:
            password = request.POST.get("InputPassword").strip()
            passowrd2 = request.POST.get("RepeatPassword").strip()
            if passowrd2!=password:
                dict = {"err": "重复密码不一致！"}
                return JsonResponse(dict)
        except Exception as e:
            dict = {"err": "密码输入错误！"}
            return JsonResponse(dict)
        try:
            username = request.POST.get("InputUsername").strip()
        except Exception as e:
            dict = {"err": "姓名输入错误！"}
            return JsonResponse(dict)
        if not User.objects.filter(username=username).exists():
            new_obj = User.objects.create_user(username=username,email=email, password=password)
            dict = {"err": "注册成功！点击前往确认登陆！","statu":1}
        else:
            dict = {"err": "用户已存在！"}
        return JsonResponse(dict)

@csrf_exempt
def login(request):
    if request.method=="GET":
        return render(request,"login/login.html")
    else:
        try:
            username = request.POST.get("InputUsername").strip()
        except Exception as e:
            dict= {"err":"email输入错误！"}
            return JsonResponse(dict)
        try:
            passowrd = request.POST.get("InputPassword").strip()
        except Exception as e:
            dict = {"err": "密码输入错误！"}
            return JsonResponse( dict)
        user_obj = auth.authenticate(username=username, password=passowrd)
        if user_obj:
            auth.login(request, user_obj)
            dict= {"statu":1,"err":"登陆成功！"}
        else:
            dict= {"err":"登陆失败！"}
        return JsonResponse( dict)

@csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect("/login")