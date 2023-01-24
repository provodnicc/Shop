from django.urls import path
from .views import AddToCartAPIView, RemoveFromCartAPIView, RemoveSingleProductFromCartAPIView

urlpatterns = [
    path('add/<int:pk>/', AddToCartAPIView.as_view(), name='add-to-cart'),
    path('remove/<int:pk>/', RemoveFromCartAPIView.as_view(), name='remove-from-cart'),
    path('remove-single/<int:pk>/', RemoveSingleProductFromCartAPIView.as_view(), name='remove-single-from-cart'),
]
