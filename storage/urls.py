from django.urls import path
from .views import StorageListAPIView, StorageCreateAPIView, StorageRetrieveUpdateDestroyAPIView, StorageChangeProductQuantityAPIView

urlpatterns = [
    path('list/', StorageListAPIView.as_view(), name='storage-list'),
    path('create/', StorageCreateAPIView.as_view(), name='storage-create'),
    path('<int:pk>/', StorageRetrieveUpdateDestroyAPIView.as_view(), name='storage-update'),
    path('change_quantity/<int:pk>/', StorageChangeProductQuantityAPIView.as_view(), name='change-quantity'),
]
