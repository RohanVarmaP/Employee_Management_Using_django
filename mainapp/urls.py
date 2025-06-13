# mainapp/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apis.urls')),  # Mount all APIs under /api/
]
