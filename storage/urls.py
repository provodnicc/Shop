from django.urls import path
from .views import StorageListAPIView, StorageCreateAPIView

urlpatterns = [
    path('list/', StorageListAPIView.as_view(), name='storage-list'),
    path('create/', StorageCreateAPIView.as_view(), name='storage-create'),
]
