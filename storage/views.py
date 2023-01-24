from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from products.models import Product
from .serializers import StorageListSerializer, StorageCreateSerializer, StorageUpdateSerializer
from .models import Storage
from rest_framework import generics, views, status


class StorageListAPIView(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageListSerializer


class StorageCreateAPIView(generics.CreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateSerializer


class StorageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageUpdateSerializer


class StorageChangeProductQuantityAPIView(views.APIView):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        quantity = request.data['quantity']
        storage = Storage.objects.get(product_id=pk)
        storage.quantity = quantity
        storage.status = 'In Stock'
        storage.save()
        return Response({'message': 'Product quantity in storage was changed'})


