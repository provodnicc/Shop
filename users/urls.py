from django.urls import path
from .views import UserCreationAPIView, UserLoginAPIView, RefreshTokenAPIView

urlpatterns = [
    path('register/', UserCreationAPIView.as_view(), name='register-user'),
    path('token/', UserLoginAPIView.as_view(), name='user-login'),
    path('token/refresh/', RefreshTokenAPIView.as_view(), name='token-refresh'),

]
