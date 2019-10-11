from django.urls import path, include
from rest_framework import routers
from apps.programs.views import *


router = routers.DefaultRouter()
router.register(r'programming', ProgramPutView)
router.register(r'programmingdate', ProgramDateView)
router.register(r'programmingprescription', ProgramPrescriptionView)
router.register(r'programmingdocument', ProgramDocumentView)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth-', include('rest_framework.urls', namespace='rest_framework')),
]
# urlpatterns = [
#     path('shops/', ShopListView.as_view(), name='shop_list'),
#     path('categorys/', CategoryListView.as_view(), name='category_list'),
# ]
