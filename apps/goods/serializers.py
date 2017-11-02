# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-11-02 19:31'

from goods.models import Goods

from rest_framework import serializers


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()

    def create(self, validated_data):
        return Goods.objects.create(**validated_data)
