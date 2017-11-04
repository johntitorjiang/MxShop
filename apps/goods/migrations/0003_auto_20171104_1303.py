# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-04 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_goodscategorybrand_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsimage',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_front_image',
            field=models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='image',
            field=models.ImageField(max_length=200, upload_to='brands/'),
        ),
    ]
