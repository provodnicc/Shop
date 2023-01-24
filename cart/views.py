from django.utils import timezone
from products.models import Product
from .models import ProductOrder, Order
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from storage.models import Storage


class AddToCartAPIView(views.APIView):
    """Add product to cart or increase its quantity"""

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        storage = Storage.objects.get(product_id=pk)
        if not storage.is_available:
            storage.status = 'Pending'
            storage.save()
            return Response({'message': 'Product is out of stock'}, status=status.HTTP_404_NOT_FOUND)
        product_order, created = ProductOrder.objects.get_or_create(
            product=product,
            user=request.user,
            ordered=False
        )
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.products.filter(product__pk=pk).exists():
                product_order.quantity += 1
                storage.quantity -= 1
                if storage.quantity == 0:
                    storage.status = 'Pending'
                product_order.save()
                storage.save()
                return Response({'message': 'Product quantity was updated'}, status=status.HTTP_200_OK)
            else:
                order.products.add(product_order)
                storage.quantity -= 1
                if storage.quantity == 0:
                    storage.status = 'Pending'
                storage.save()
                return Response({'message': 'Product was successfully added to cart'}, status=status.HTTP_200_OK)
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(
                user=request.user,
                ordered_date=ordered_date
            )
            order.products.add(product_order)
            storage.quantity -= 1
            if storage.quantity == 0:
                storage.status = 'Pending'
            storage.save()
            return Response({'message': 'Product was successfully added to cart'})


class RemoveFromCartAPIView(views.APIView):
    """Remove product from cart without decreasing its quantity"""

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        order_qs = Order.objects.filter(
            user=request.user,
            ordered=False
        )
        if order_qs.exists():
            order = order_qs[0]
            if order.products.filter(product__pk=pk).exists():
                product_order = ProductOrder.objects.filter(
                    product=product,
                    user=request.user,
                    ordered=False
                )[0]
                storage = Storage.objects.get(product_id=pk)
                if storage.is_available:
                    storage.quantity = product_order.quantity
                    storage.save()
                else:
                    storage.quantity = product_order.quantity
                    storage.status = 'In Stock'
                    storage.save()
                order.products.remove(product_order)
                product_order.delete()
                return Response({'message': 'Product was removed from cart'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'This product was not in your cart'})
        else:
            return Response({'message': 'You do not have an active order'})


class RemoveSingleProductFromCartAPIView(views.APIView):
    """Remove product by decreasing its quantity"""

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        storage = Storage.objects.get(product_id=pk)
        order_qs = Order.objects.filter(
            user=request.user,
            ordered=False
        )
        if order_qs.exists():
            order = order_qs[0]
            if order.products.filter(product__pk=pk).exists():
                product_order = ProductOrder.objects.filter(
                    product=product,
                    user=request.user,
                    ordered=False
                )[0]
                if product_order.quantity > 1:
                    product_order.quantity -= 1
                    if not storage.is_available:
                        storage.quantity += 1
                        storage.status = 'In Stock'
                        storage.save()
                    else:
                        storage.quantity += 1
                        storage.save()
                    product_order.save()
                else:
                    if not storage.is_available:
                        storage.quantity += 1
                        storage.status = 'In Stock'
                        storage.save()
                    else:
                        storage.quantity += 1
                        storage.save()
                    order.products.remove(product_order)
                    product_order.delete()
                return Response({'message': 'Product quantity was updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'This product was not in your cart'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'You do not have an active order'}, status=status.HTTP_404_NOT_FOUND)
