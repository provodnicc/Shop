from rest_framework import generics
from .models import Category, Product
from .serializers import \
    (CategoryListRetrieveDeleteSerializer,
     CategoryCreateUpdateSerializer,
     ProductListRetrieveDestroySerializer,
     ProductCreateUpdateSerializer,
     )


##############
##Categories##
##############

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListRetrieveDeleteSerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateUpdateSerializer


class CategoryUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateUpdateSerializer


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListRetrieveDeleteSerializer


class CategoryDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListRetrieveDeleteSerializer


##############
##Products##
##############

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListRetrieveDestroySerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer


class ProductUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListRetrieveDestroySerializer


class ProductDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListRetrieveDestroySerializer
