from rest_framework import serializers
from .models import Category, Product


class CategoryParentFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class CategorySerializer(serializers.ModelSerializer):
    parent = CategoryParentFieldSerializer()

    class Meta:
        model = Category
        # depth = 10
        fields = ('title', 'parent',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'category', 'description', 'price', 'image')
