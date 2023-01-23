from rest_framework import generics, views, status
from rest_framework.response import Response

from .models import Category, Product
from .serializers import \
    (CategoryListRetrieveDeleteSerializer,
     CategoryCreateUpdateSerializer,
     ProductListRetrieveDestroySerializer,
     ProductCreateUpdateSerializer,
     )
from storage.models import Storage, PRODUCT_STATUSES


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


class ProductCreateAPIView(views.APIView):
    def post(self, request):
        serializer = ProductCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product = Product.objects.create(**serializer.validated_data)
            storage = Storage.objects.create(product=product)
            product.save()
            storage.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListRetrieveDestroySerializer


class ProductDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListRetrieveDestroySerializer
