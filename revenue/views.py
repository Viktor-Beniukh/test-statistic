from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from revenue.models import RevenueStatistic


class RevenueStatisticView(APIView):
    def get(self, request):
        queryset = RevenueStatistic.objects.values("name", "date").annotate(
            total_revenue=Sum("revenue"),
            total_spend=Sum("spend__spend"),
            total_impressions=Sum("spend__impressions"),
            total_clicks=Sum("spend__clicks"),
            total_conversion=Sum("spend__conversion"),
        )
        return Response(queryset)
