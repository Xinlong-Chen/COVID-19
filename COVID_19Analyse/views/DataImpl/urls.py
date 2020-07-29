from django.urls import path

from .api import confirmAmplification as Confirm
from .api import overseaTrend as Trend
from .api import rank as Rank
from .api import today as Today
from .api import details as Details
from .api import summarize as Sum

app_name = 'api'
urlpatterns = [
    path('details/',Details.getCountryDetails,name='details'),
    path('sumdetails/',Details.getSumDetails,name='sumdetails'),
    path('mainCountry/',Details.getMainCountryDetails,name='mainCountry'),
    path('oversea/',Confirm.overseaConfirm,name='oversea'),
    path('plc/',Confirm.peopleLargeCountryConfirm,name='plc'),
    path('continent/',Confirm.continentConfirm,name='continent'),
    path('trend/',Trend.getOverseaTrend,name='trend'),
    path('deadrank/', Rank.getDeadRank, name='deadRank'),
    path('healrank/', Rank.getHealRank, name='healRank'),
    path('confirmrank/', Rank.getConfirmRank, name='confirmRank'),
    path('confirmrate/',Rank.getconfirmAmpl,name='confirmRate'),
    path('sum/',Sum.getSummarize,name='sum'),
    path('today/',Today.getToday,name='today'),
]