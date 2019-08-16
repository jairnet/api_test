from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken import views
# from apps.shop import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.shop.urls')),
    path('api_generate_token/', views.obtain_auth_token),
]
