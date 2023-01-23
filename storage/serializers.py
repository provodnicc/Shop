from .models import Storage
from rest_framework import serializers
from products.serializers import ProductListRetrieveDestroySerializer


class StorageListSerializer(serializers.ModelSerializer):
    product = ProductListRetrieveDestroySerializer()

    class Meta:
        model = Storage
        fields = ('id', 'product', 'quantity', 'status')


class StorageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ('product', 'quantity', 'status')


class StorageUpdateSerializer(serializers.ModelSerializer):
    product = ProductListRetrieveDestroySerializer(read_only=True)

    class Meta:
        model = Storage
        fields = ('product', 'quantity', 'status')
