# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-11-02 23:08'

import django_filters

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    price_min = django_filters.NumberFilter(name="shop_price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(name="shop_price", lookup_expr="lte")
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']
