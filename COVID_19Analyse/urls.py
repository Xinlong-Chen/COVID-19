from django.urls import path,include

from .views.FileDownload import FileDownload as Down
from .views import UpdateView as Update
from .views import views

app_name = 'covid19'
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path('download/', Down.download_file, name="download"),
    path('maincountry/', views.maincountry, name="maincountry"),
    path('continent/', views.continent, name="continent"),
    path('rank/', views.rank, name="rank"),
    path('trend/', views.trend, name="trend"),
    path("all/", views.covidindex, name="all"),
    path('update/', Update.update, name='update'),
    path('details/<country>', views.details, name='details'),

    # 二级路由 api 数据接口
    path('api/', include('COVID_19Analyse.views.DataImpl.urls')),
]
