from rest_framework import serializers
from .models import Category, Product


##############
##Categories##
##############

class CategoryParentFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)


class CategoryListRetrieveDeleteSerializer(serializers.ModelSerializer):
    parent = CategoryParentFieldSerializer()

    class Meta:
        model = Category
        # depth = 10
        fields = ('id', 'title', 'parent',)


class CategoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'parent')


##############
##Products##
##############

class ProductListRetrieveDestroySerializer(serializers.ModelSerializer):
    category = CategoryParentFieldSerializer()

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'description', 'price', 'image')


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'category', 'description', 'price', 'image')
