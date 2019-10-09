import json
import time
import uuid
from datetime import date, datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework import viewsets

from .models import Program
from apps.addressing.models import Address
from .serializer import ProgramSerializer

# Create your views here.


class ProgramListView(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    # def provider_object(self, )

    def put(self, request):
        nit = self.request.headers.get('nit')
        token = self.request.headers.get('token')
        uuidProg = str(uuid.uuid1()).replace('-', '')
        today = datetime.today()
        if nit and token:
            # body_unicode = request.body.decode('utf-8')
            # body = json.loads(body_unicode)
            # content = body
            validated_data = request.data
            object_addressing = Address.objects.get(id=request.data['id'])
            validated_data.pop('id')
            validated_data['IDProgramacion'] = uuidProg
            validated_data['NoPrescripcion'] = object_addressing.NoPrescripcion
            validated_data['TipoTec'] = object_addressing.TipoTec
            validated_data['ConTec'] = object_addressing.ConTec
            validated_data['TipoIDPaciente'] = object_addressing.TipoIdPaciente
            validated_data['NoIdPaciente'] = object_addressing.NoIdPaciente
            validated_data['NoEntrega'] = object_addressing.NoEntrega
            validated_data['FecProgramacion'] = today.strftime('%Y-%m-%d-%H:%M')
            validated_data['EstProgramacion'] = (today + timedelta(days=10)).strftime('%Y-%m-%d-%H:%M')
            validated_data['FechaAnulacion'] = (today + timedelta(days=15)).strftime('%Y-%m-%d-%H:%M')
            object_create = Program.objects.create(**validated_data)           
            return Response({"Id": object_create.id, "IDProgramacion": object_create.IDProgramacion})
            # return Response({"success": "Number of Programming '{}' ".format('OK')})
        return json.dumps({'error':'requeride nit, token and date'})