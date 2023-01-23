from .serializers import StorageListRetrieveDestroySerializer, StorageCreateUpdateSerializer
from .models import Storage
from rest_framework import generics


class StorageListAPIView(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageListRetrieveDestroySerializer


class StorageCreateAPIView(generics.CreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateUpdateSerializer

