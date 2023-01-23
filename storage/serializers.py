from .models import Storage
from rest_framework import serializers
from products.serializers import ProductListRetrieveDestroySerializer


class StorageListRetrieveDestroySerializer(serializers.ModelSerializer):
    product = ProductListRetrieveDestroySerializer()

    class Meta:
        model = Storage
        fields = ('product', 'quantity', 'status')


class StorageCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ('product', 'quantity', 'status')
