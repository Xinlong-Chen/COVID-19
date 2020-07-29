from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'COVID_19Analyse/index.html')

@login_required
def covidindex(request):
    return render(request, 'COVID_19Analyse/main.html')

@login_required
def dashboard(request):
    context = {'username': request.user.username}
    return render(request, 'COVID_19Analyse/Dashboard.html',context)

@login_required
def rank(request):
    context = {'username': request.user.username}
    return render(request, 'COVID_19Analyse/Rank.html',context)

@login_required
def trend(request):
    context = {'username': request.user.username}
    return render(request, 'COVID_19Analyse/Trend.html',context)

@login_required
def maincountry(request):
    context = {'username': request.user.username}
    return render(request, 'COVID_19Analyse/MainCountry.html',context)

@login_required
def continent(request):
    context = {'username': request.user.username}
    return render(request, 'COVID_19Analyse/Continent.html',context)

@login_required
def details(request,country):
    context = {'username': request.user.username,'country':country}
    return render(request, 'COVID_19Analyse/details.html',context)