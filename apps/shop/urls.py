from django.urls import path, include
from rest_framework import routers
from apps.shop.views import *


router = routers.DefaultRouter()
router.register(r'shops', ShopListView)
router.register(r'categorys', CategoryListView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth-', include('rest_framework.urls', namespace='rest_framework')),
    # path('shops/<int:pk>', views.ShopDetail, name='shops_detail'),
    # path('categories', views.CategoryList, name='categories'),
    # path('categories/<int:pk>', views.CategoryDetail, name='categories_detail'),
]

