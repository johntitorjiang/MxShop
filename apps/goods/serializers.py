# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-11-02 19:31'

from goods.models import Goods, GoodsCategory

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"
