from django.urls import path, include
from rest_framework import routers
# from django.urls import path
from apps.addressing.views import *


router = routers.DefaultRouter()
router.register(r'address', AddressListView)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth-', include('rest_framework.urls', namespace='rest_framework')),
]
# urlpatterns = [
#     path('shops/', ShopListView.as_view(), name='shop_list'),
#     path('categorys/', CategoryListView.as_view(), name='category_list'),
# ]

