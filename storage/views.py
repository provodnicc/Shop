from .serializers import StorageListSerializer, StorageCreateSerializer, StorageUpdateSerializer
from .models import Storage
from rest_framework import generics


class StorageListAPIView(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageListSerializer


class StorageCreateAPIView(generics.CreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateSerializer


class StorageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageUpdateSerializer
