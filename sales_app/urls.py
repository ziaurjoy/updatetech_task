
from rest_framework.routers import DefaultRouter
from . import views

from django.urls import path


router = DefaultRouter()
router.register(r'sales-viewset', views.SalesViewSet, basename='sales-viewset')
urlpatterns = router.urls


urlpatterns = [
    path('total-number-of-oders-count-per-year', views.TotalNumberOfOrdersCountPerYearView.as_view(), name='api-total-number-of-oders-count-per-year'),
    path('total-count-of-distric-customer', views.TotalCountOfDistinctCustomersView.as_view(), name='total-count-of-distric-customer'),
    path('top-3-of-customer-transaction', views.Top3CustomerstotalAmountOfTransactionsView.as_view(), name='top-3-of-customer-transaction'),
    path('customer-transaction-per-year', views.CustomerTransactionsPerYearReportView.as_view(), name='customer-transaction-per-year'),
    path('most-selling-sub-categories', views.MostSellingItemsSubCategoryView.as_view(), name='most-selling-sub-categories'),
    path('region-base-sales-performance-pie-chat', views.RegionBasisSalesPerformancePieChartView.as_view(), name='region-base-sales-performance-pie-chat'),
    path('sales-performance-line-chart-of-years', views.SalesPerformanceLineChartOverTheYearsView.as_view(), name='sales-performance-line-chart-years'),

    # this return for pdf report file
    path('sales-performance-line-chart-of-years-report-pdf', views.RegionBasisSalesPerformancePieChartReportView.as_view(), name='sales-performance-line-chart-years-report-pdf'),
]

