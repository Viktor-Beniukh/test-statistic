import json

from django.test import TestCase
from django.urls import reverse

from revenue.models import RevenueStatistic
from spend.models import SpendStatistic


REVENUE_URL = reverse("revenue:revenue-statistics")


class RevenueModelsTest(TestCase):

    def test_spend_statistic_str(self) -> None:
        revenue_statistic = RevenueStatistic.objects.create(
            name="Test Name 1",
            date="2023-09-27",
            revenue=200,
        )
        self.assertEqual(str(revenue_statistic), revenue_statistic.name)


class RevenueStatisticViewTestCase(TestCase):
    def setUp(self):
        spend_statistic = SpendStatistic.objects.create(
            name="Test Name 1",
            date="2023-09-27",
            spend=100,
            impressions=500,
            clicks=50,
            conversion=5,
        )

        RevenueStatistic.objects.create(
            name="Test Name 1",
            date="2023-09-27",
            revenue=200,
            spend=spend_statistic,
        )

    def test_revenue_statistic_view_status_code(self):
        response = self.client.get(REVENUE_URL)
        self.assertEqual(response.status_code, 200)

    def test_revenue_statistic_view_content(self):
        response = self.client.get(REVENUE_URL)
        self.assertContains(response, "Test Name 1")
        self.assertContains(response, "2023-09-27")
        self.assertContains(response, 200)

    def test_revenue_statistic_view_aggregation(self):
        response = self.client.get(REVENUE_URL)
        data = json.loads(response.content.decode("utf-8"))

        self.assertEqual(data[0]["name"], "Test Name 1")
        self.assertEqual(data[0]["date"], "2023-09-27")
        self.assertEqual(data[0]["total_revenue"], 200.00)
        self.assertEqual(data[0]["total_spend"], 100.00)
        self.assertEqual(data[0]["total_impressions"], 500)
        self.assertEqual(data[0]["total_clicks"], 50)
        self.assertEqual(data[0]["total_conversion"], 5)
