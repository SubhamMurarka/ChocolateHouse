from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chocolate/', include('chocolate.urls')),  # Include chocolate app URLs
]
