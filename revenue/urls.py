from django.urls import path

from revenue.views import RevenueStatisticView

app_name = "revenue"

urlpatterns = [
    path("revenue-statistics/", RevenueStatisticView.as_view(), name="revenue-statistics"),
]
