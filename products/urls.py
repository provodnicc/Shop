from django.urls import path
from .views import \
    (CategoryListAPIView,
     CategoryCreateAPIView,
     CategoryUpdateAPIView,
     CategoryRetrieveAPIView,
     CategoryDestroyAPIView,
     ProductListAPIView,
     ProductCreateAPIView,
     ProductRetrieveAPIView,
     ProductUpdateAPIView,
     ProductDestroyAPIView,
     )

urlpatterns = [
    # categories
    path('categories/list/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category-retrieve'),
    path('categories/<int:pk>/delete/', CategoryDestroyAPIView.as_view(), name='category-destroy'),

    # products
    path('list/', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-retrieve'),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view(), name='product-delete'),
]
