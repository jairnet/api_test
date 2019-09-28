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
    
    def create(self, validated_data):
        dict_data = self.context['request'].data
        if dict_data.get('id', False):
            query_set = Category.objects.filter(id = dict_data['id'])
            if query_set:
                raise NameError('ID of category is duplicate. \n')
        return Category.objects.create(**validated_data)