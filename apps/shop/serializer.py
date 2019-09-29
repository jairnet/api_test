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
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Category` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance
