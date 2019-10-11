import json
import time
import uuid
from datetime import date, datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework import viewsets

from .models import Program
from apps.addressing.models import Address
from .serializer import ProgramSerializer


class ProgramPutView(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def put(self, request):
        nit = self.request.headers.get('nit')
        token = self.request.headers.get('token')
        uuidProg = str(uuid.uuid1()).replace('-', '')
        today = datetime.today()
        if nit and token:
            validated_data = request.data
            id_address = request.data['id']
            try:
                object_addressing = Address.objects.get(id=id_address)
            except ObjectDoesNotExist:
                return Response(
                    {"Error": "Addressing with ID {0} no found "
                    .format(id_address)})
            validated_data.pop('id')
            validated_data['IDProgramacion'] = uuidProg
            validated_data['NoPrescripcion'] = object_addressing.NoPrescripcion
            validated_data['TipoTec'] = object_addressing.TipoTec
            validated_data['ConTec'] = object_addressing.ConTec
            validated_data['TipoIDPaciente'] = object_addressing.TipoIdPaciente
            validated_data['NoIdPaciente'] = object_addressing.NoIdPaciente
            validated_data['NoEntrega'] = object_addressing.NoEntrega
            validated_data['FecProgramacion'] = today.strftime('%Y-%m-%d')
            validated_data['EstProgramacion'] = (today + timedelta(days=10)).strftime('%Y-%m-%d-%H:%M')
            validated_data['FechaAnulacion'] = (today + timedelta(days=15)).strftime('%Y-%m-%d-%H:%M')
            object_create = Program.objects.create(**validated_data)
            Address.objects.filter(id=id_address).delete()           
            return Response({"Id": object_create.id, "IDProgramacion": object_create.IDProgramacion})
        return Response({'error':'requeride nit, token and date'})


class ProgramDateView(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def get_queryset(self):
        nit = self.request.headers.get('nit')
        token = self.request.headers.get('token')
        date_request = self.request.headers.get('date')
        if nit and token and date_request:
            date_list = date_request.split('-')
            queryset = Program.objects.filter(FecProgramacion=date_request)
            return queryset
        return Response({'error':'requeride nit, token and date'})


class ProgramPrescriptionView(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def get_queryset(self):
        nit = self.request.headers.get('nit')
        token = self.request.headers.get('token')
        prescription = self.request.headers.get('noPrescripcion')
        if nit and token and prescription:
            queryset = Program.objects.filter(NoPrescripcion=prescription)
            return queryset
        return Response({'error':'requeride nit, token and prescription'})


class ProgramDocumentView(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def get_queryset(self):
        nit = self.request.headers.get('nit')
        token = self.request.headers.get('token')
        tipodoc = self.request.headers.get('tipodoc')
        numdoc = self.request.headers.get('numdoc')
        if nit and token and tipodoc and numdoc:
            queryset = Program.objects.filter(TipoIDPaciente=tipodoc,
                NoIdPaciente=numdoc)
            return queryset
        return Response({'error':'requeride nit, token, type document and ducument number'})
