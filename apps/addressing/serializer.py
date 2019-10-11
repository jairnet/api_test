from rest_framework import serializers
from apps.addressing.models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id', 'NoPrescripcion', 'TipoTec', 'ConTec', 'TipoIdPaciente', 'NoIdPaciente', 'NoEntrega',
            'NoSubEntrega', 'TipoIDProv', 'NoIDProv', 'CodMunEnt', 'FecMaxEnt', 'CantTotAEntregar',
            'DirPaciente', 'CodSerTecAEntregar',
            ]

    # def create(self, validated_data):
    #     dict_data = self.context['request'].data
    #     if dict_data.get('id', False):
    #         query_set = Category.objects.filter(id = dict_data['id'])
    #         if query_set:
    #             raise NameError('ID of category is duplicate. \n')
    #     return Category.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Category` instance, given the validated data.
    #     """
        
    #     TipoTec
    #     ConTec
    #     TipoIdPaciente
    #     NoIdPaciente
    #     NoEntrega
    #     NoSubEntrega
    #     TipoIDProv
    #     NoIDProv
    #     CodMunEnt
    #     FecMaxEnt
    #     CantTotAEntregar
    #     DirPaciente
    #     CodSerTecAEntregar
    #     instance.NoPrescripcion = validated_data.get('id', instance.id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.save()
    #     return instance
