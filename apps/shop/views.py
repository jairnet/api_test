from .models import Category, Shop
from .serializer import CategorySerializer, ShopSerializer
from rest_framework import viewsets


class ShopListView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


# class ShopDetailView(viewsets.ModelViewSet):
#     queryset = Shop.objects.all()
#     serializer_class = ShopSerializer


class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class CategoryDetailView(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
