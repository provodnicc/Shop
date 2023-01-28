from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Category, Product
from .serializers import \
    (CategoryListRetrieveDeleteSerializer,
     CategoryCreateUpdateSerializer,
     ProductListRetrieveDestroySerializer,
     ProductCreateUpdateSerializer,
     )
from storage.models import Storage


##############
##Categories##
##############

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListRetrieveDeleteSerializer
    permission_classes = [IsAuthenticated]


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateUpdateSerializer
    permission_classes = [IsAdminUser]


class CategoryUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateUpdateSerializer
    permission_classes = [IsAdminUser]


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListRetrieveDeleteSerializer
    permission_classes = [IsAuthenticated]


class CategoryDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListRetrieveDeleteSerializer
    permission_classes = [IsAdminUser]


##############
##Products##
##############

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListRetrieveDestroySerializer
    permission_classes = [IsAuthenticated]


class ProductCreateAPIView(views.APIView):
    def post(self, request):
        serializer = ProductCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product = Product.objects.create(**serializer.validated_data)
            storage = Storage.objects.create(product=product)
            product.save()
            storage.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    permission_classes = [IsAdminUser]


class ProductUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer
    permission_classes = [IsAdminUser]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListRetrieveDestroySerializer
    permission_classes = [IsAuthenticated]


class ProductDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListRetrieveDestroySerializer
    permission_classes = [IsAdminUser]
