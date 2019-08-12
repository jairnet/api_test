from django.urls import path, include
from django.contrib import admin
from apps.shop import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.shop.urls')),
]
