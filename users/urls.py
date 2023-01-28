from django.urls import path
from .views import UserCreationAPIView, UserLoginAPIView, RefreshTokenAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.urls import include

urlpatterns = [
    path('register/', UserCreationAPIView.as_view(), name='register-user'),
    path('token/', UserLoginAPIView.as_view(), name='user-login'),
    path('token/refresh/', RefreshTokenAPIView.as_view(), name='token-refresh'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
