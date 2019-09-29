import json
import time
from datetime import date

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework import viewsets

from .models import Address
from .serializer import AddressSerializer


class AddressListView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        nit = self.request.headers.get('nit')
        token = self.request.headers.get('token')
        if nit and token and date_list:
            date_list = self.request.headers.get('date').split('-')
            year = int(date_list[0])
            month = int(date_list[1])
            day = int(date_list[2])
            date_address = date(year, month, day)
            queryset = Address.objects.filter(nit=nit, token=token, date_address=date_address)
            return queryset
        return Response({'error':'requeride nit, token and date'})

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
