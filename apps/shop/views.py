from django.shortcuts import render, get_object_or_404
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


class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def put(self, request):
        saved_category = Category.objects.all()
        pk = request.data.get('id', False)
        saved_category = get_object_or_404(Category.objects.all(), pk=pk)
        data = request.data
        serializer = CategorySerializer(instance=saved_category, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"success": "Category '{}' updated successfully".format(category_saved.name)})

# class CategoryListView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer