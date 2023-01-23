from django.urls import path
from .views import CategoryListAPIView, ProductListAPIView

urlpatterns = [
    # categories
    path('categories/list/', CategoryListAPIView.as_view(), name='category-list'),

    # products
    path('list/', ProductListAPIView.as_view(), name='product-list'),
]