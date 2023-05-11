
from sales_app.views import SalesViewSet, QueryViewSet, SalesReportTotalNumberOfOdersCountPerYearReportViewView, TotalCountOfDistinctCustomersViewView, Top3CustomerstotalAmountOfTransactionsViewView, CustomerTransactionsPerYearReportViewView, MostSellingItemsSubCategoryNamesView, RegionBasisSalesPerformancePieChartView,SalesPerformanceLineChartOverTheYearsView
from rest_framework.routers import DefaultRouter

from django.urls import path


router = DefaultRouter()
router.register(r'api', SalesViewSet, basename='sales-api')
router.register(r'api-query', QueryViewSet, basename='sales-query-api')
urlpatterns = router.urls

urlpatterns = [
    path('total-number-of-oders-count-per-year/', SalesReportTotalNumberOfOdersCountPerYearReportViewView.as_view(), name='api-total-number-of-oders-count-per-year'),
    path('total-count-of-distric-customer/', TotalCountOfDistinctCustomersViewView.as_view(), name='total-count-of-distric-customer'),
    path('top-3-of-customer-transaction/', Top3CustomerstotalAmountOfTransactionsViewView.as_view(), name='top-3-of-customer-transaction'),
    path('customer-transaction-per-year/', CustomerTransactionsPerYearReportViewView.as_view(), name='customer-transaction-per-year'),
    path('most-selling-sub-categories/', MostSellingItemsSubCategoryNamesView.as_view(), name='most-selling-sub-categories'),
    path('region-base-sales-performance-pie-chat/', RegionBasisSalesPerformancePieChartView.as_view(), name='region-base-sales-performance-pie-chat'),
    path('sales-performance-line-chart-years/', SalesPerformanceLineChartOverTheYearsView.as_view(), name='sales-performance-line-chart-years'),
]

