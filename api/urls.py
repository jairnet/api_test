from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.shop.urls')),
    path('api/', include('apps.addressing.urls')),
    path('api_generate_token/', views.obtain_auth_token),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
