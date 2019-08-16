from django.urls import path, include
from rest_framework import routers
# from django.urls import path
from apps.shop.views import *


router = routers.DefaultRouter()
router.register(r'shops', ShopListView)
router.register(r'categorys', CategoryListView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth-', include('rest_framework.urls', namespace='rest_framework')),
]
# urlpatterns = [
#     path('shops/', ShopListView.as_view(), name='shop_list'),
#     path('categorys/', CategoryListView.as_view(), name='category_list'),
# ]

