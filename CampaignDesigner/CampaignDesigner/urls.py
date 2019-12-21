from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='main')),
    path('auth/', include('authapp.urls', namespace='auth'))
]
