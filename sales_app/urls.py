
from sales_app.views import SalesViewSet, QueryViewSet
from rest_framework.routers import DefaultRouter

from django.urls import path


router = DefaultRouter()
router.register(r'api', SalesViewSet, basename='sales-api')
router.register(r'api-query', QueryViewSet, basename='sales-query-api')
urlpatterns = router.urls

# urlpatterns = [
#     path('admin/', QueryViewSet.as_view()),

# ]

