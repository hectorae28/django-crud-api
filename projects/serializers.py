from rest_framework import serializers
from .models import *


class MeniItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['id', 'name', 'description', 'price',]


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'isSell', 'note', 'date_create', 'menu_item', 'order']
        read_only_fields = ['date_create',]


class OrdersSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True)

    class Meta:
        model = Orders
        fields = ['id', 'name', 'last_name', 'nota',
                  'date_create', 'isPayed', 'payment_type', 'products']
        read_only_fields = ['id', 'date_create',]

    def create(self, validated_data):
        orders_data = validated_data.pop('products')
        order = Orders.objects.create(**validated_data)
        for order_data in orders_data:
            product = Products.objects.filter(
                order=1, isSell=False,).earliest('date_create')
            product.order = order
            product.isSell = True
            product.save()
        return order

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products')
        products_order = Products.objects.filter(order=instance.id)
        instance.name = validated_data.get('name')
        instance.last_name = validated_data.get('last_name')
        instance.nota = validated_data.get('nota')
        instance.isPayed = validated_data.get('isPayed')
        instance.payement_type = validated_data.get('payament_type')
        instance.save()
        if len(products_data) > products_order.count():
            for i in range(products_order.count(), len(products_data)):
                product = Products.objects.filter(
                    order=1, isSell=False,).earliest('date_create')
                product.order = instance
                product.isSell = True
                product.save()
        elif len(products_data) < products_order.count():
            NanOrder = Orders.objects.get(id=1)
            for i in range(len(products_data), products_order.count()):
                product = Products.objects.filter(
                    order=instance).earliest('-date_create')
                product.order = NanOrder
                product.isSell = False
                product.save()
        return instance
