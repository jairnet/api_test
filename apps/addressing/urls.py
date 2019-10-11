from django.urls import path, include
from rest_framework import routers
# from django.urls import path
from apps.addressing.views import *


router = routers.DefaultRouter()
router.register(r'addressdate', AddressDateView)
router.register(r'addressprescription', AddressPrescriptionView)
router.register(r'addressdocument', AddressDocumentView)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth-', include('rest_framework.urls', namespace='rest_framework')),
]
