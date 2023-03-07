from rest_framework import routers
from django.urls import path, include
from .api import *

router = routers.DefaultRouter()
router.register('menu',MenuItemViewSet,'menu')
router.register('products',ProductsViewSet,'products')
router.register('orders',OrdersViewSet,'order_product')


urlpatterns=[
    path('',include(router.urls)),
    path('week/',OrdersMonthView.as_view()),
]