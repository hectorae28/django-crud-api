from rest_framework import viewsets
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItems.objects.all()
    serializer_class = MeniItemSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated]


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, pk=None):
        order = Orders.objects.filter(id=pk)
        NanOrder = Orders.objects.get(id=1)
        products_order = Products.objects.filter(order=pk)
        order_serializer = OrdersSerializer(order, many=True)
        for product_order in products_order:
            product_order.order = NanOrder
            product_order.isSell = False
            product_order.save()
        order.delete()
        return Response(order_serializer.data, status=status.HTTP_200_OK)


class OrdersMonthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format):
        date = datetime.now()
        order = Orders.objects.filter(date_create__month=date.month)
        order_serializer = OrdersSerializer(order, many=True)
        return Response(order_serializer.data, status=status.HTTP_200_OK)
