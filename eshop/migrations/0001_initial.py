# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 03:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('introduction', models.TextField()),
                ('score', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_images', related_query_name='goods_image', to='eshop.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Remittance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='RemittanceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('remittance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remittance_items', related_query_name='remittance_item', to='eshop.Remittance')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('introduction', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('address', models.CharField(max_length=255)),
                ('score', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Webuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_owner', models.BooleanField()),
                ('nickname', models.CharField(max_length=20)),
                ('gender', models.BooleanField()),
                ('age', models.IntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('ori_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='real_user', related_query_name='real_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='shoppingcartitem',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoppingCart', related_query_name='shoppingCartItem', to='eshop.Webuser'),
        ),
        migrations.AddField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', related_query_name='shop', to='eshop.Webuser'),
        ),
        migrations.AddField(
            model_name='remittance',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remittances', related_query_name='remittance', to='eshop.Webuser'),
        ),
        migrations.AddField(
            model_name='remittance',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remittances', related_query_name='remittance', to='eshop.Shop'),
        ),
        migrations.AddField(
            model_name='goods',
            name='RemittanceItem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='remittanceitem_goods', related_query_name='remittanceitem_goods', to='eshop.RemittanceItem'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_goods', related_query_name='type_goods', to='eshop.Type'),
        ),
        migrations.AddField(
            model_name='goods',
            name='keywords',
            field=models.ManyToManyField(related_name='keyword_goods', related_query_name='keyword_goods', to='eshop.Keyword'),
        ),
        migrations.AddField(
            model_name='goods',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', related_query_name='shop_goods', to='eshop.Shop'),
        ),
        migrations.AddField(
            model_name='goods',
            name='shoppingCartItem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shoppingitem_goods', related_query_name='shoppingitem_goods', to='eshop.ShoppingCartItem'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='eshop.Webuser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='eshop.Goods'),
        ),
    ]
