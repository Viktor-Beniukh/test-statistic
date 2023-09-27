from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from spend.models import SpendStatistic


class SpendStatisticView(APIView):
    def get(self, request):
        queryset = SpendStatistic.objects.values("name", "date").annotate(
            total_spend=Sum("spend"),
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversion=Sum("conversion"),
            total_revenue=Sum("revenue__revenue"),
        )
        return Response(queryset)
