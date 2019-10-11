import json
import time
from datetime import date

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework import viewsets

from .models import Address
from .serializer import AddressSerializer


class AddressDateView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        nit = self.request.headers.get('nit')
        token = self.request.headers.get('token')
        date_request = self.request.headers.get('date')
        if nit and token and date_request:
            date_list = date_request.split('-')
            year = int(date_list[0])
            month = int(date_list[1])
            day = int(date_list[2])
            date_address = date(year, month, day)
            queryset = Address.objects.filter(company__nit=nit, company__token=token, date_address=date_address)
            return queryset
        return Response({'error':'requeride nit, token and date'})


class AddressPrescriptionView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        nit = self.request.headers.get('nit')
        token = self.request.headers.get('token')
        prescription = self.request.headers.get('noPrescripcion')
        if nit and token and prescription:
            queryset = Address.objects.filter(company__nit=nit, company__token=token,
                NoPrescripcion=prescription)
            return queryset
        return Response({'error':'requeride nit, token and prescription'})


class AddressDocumentView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        nit = self.request.headers.get('nit')
        token = self.request.headers.get('token')
        tipodoc = self.request.headers.get('tipodoc')
        numdoc = self.request.headers.get('numdoc')
        if nit and token and tipodoc and numdoc:
            queryset = Address.objects.filter(company__nit=nit, company__token=token,
                TipoIdPaciente=tipodoc, NoIdPaciente=numdoc)
            return queryset
        return Response({'error':'requeride nit, token, type document and ducument number'})

# class AddressListView(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     def put(self, request):
#         saved_category = Category.objects.all()
#         pk = request.data.get('id', False)
#         saved_category = get_object_or_404(Category.objects.all(), pk=pk)
#         data = request.data
#         serializer = CategorySerializer(instance=saved_category, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             category_saved = serializer.save()
#         return Response({"success": "Category '{}' updated successfully".format(category_saved.name)})

# class CategoryListView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
