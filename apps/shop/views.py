from django.shortcuts import render
from .models import Category, Shop
from .serializer import CategorySerializer, ShopSerializer
from rest_framework.response import Response
from rest_framework import viewsets
# from rest_framework import generics


class ShopListView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_queryset(self):
        queryset = Shop.objects.filter(id=int(self.request.headers.get('id')))
        return queryset
# class ShopListView(generics.ListCreateAPIView):
#     queryset = Shop.objects.all()
#     serializer_class = ShopSerializer


class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class CategoryListView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer