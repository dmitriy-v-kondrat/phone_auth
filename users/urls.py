

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import PhoneEnterView, CodeEnterView, CustomUserProfileView

urlpatterns = [
    path('phone/', PhoneEnterView.as_view(), name='phone'),
    path('code/', CodeEnterView.as_view(), name='code'),
    path('profile/', CustomUserProfileView.as_view(), name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]