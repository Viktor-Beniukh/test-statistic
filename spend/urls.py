from django.urls import path

from spend.views import SpendStatisticView

app_name = "spend"

urlpatterns = [
    path("spend-statistics/", SpendStatisticView.as_view(), name="spend-statistics"),
]
