from django.urls import path

from customauth_app.views import CustomUserRegistrationView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'api', CustomUserViewSet, basename='custom-auth')
# urlpatterns = router.urls


urlpatterns = [
    path('registration', CustomUserRegistrationView.as_view(), name='user-registration'),
]