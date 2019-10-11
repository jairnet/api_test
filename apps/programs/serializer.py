from rest_framework import serializers
from apps.programs.models import Program


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        fields = [
            'id', 'IDProgramacion', 'NoPrescripcion', 'TipoTec', 'ConTec',
            'TipoIDPaciente', 'NoIdPaciente', 'NoEntrega', 'FecMaxEnt',
            'TipoIDSedeProv', 'NoIDSedeProv', 'CodSedeProv',
            'CodTecAEntregar', 'FecProgramacion', 'EstProgramacion',
            'FechaAnulacion',
            ]
    
    def create(self, validated_data):
        dict_data = self.context['request'].data
        # if dict_data.get('id', False):
        # query_set = .objects.filter(id = dict_data['id'])
        # if query_set:
        #     raise NameError('ID now is programming. \n')
        return Program.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.FecMaxEnt = validated_data.get('FecMaxEnt')
    #     instance.TipoIDSedeProv = validated_data.get('TipoIDSedeProv')
    #     instance.NoIDSedeProv = validated_data.get('NoIDSedeProv')
    #     instance.CodSedeProv = validated_data.get('CodSedeProv')
    #     instance.CodSerTecAEntregar = validated_data.get('CodSerTecAEntregar')
    #     instance.CantTotAEntregar = validated_data.get('CantTotAEntregar')
    #     instance.save()
    #     return instance.id
