from rest_framework import serializers
from apps.shop.models import Category, Shop


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = ['url', 'id', 'name', 'address', 'phone', 'site', 'email', 'country',
            'district', 'city', 'category', 'description']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'code']

