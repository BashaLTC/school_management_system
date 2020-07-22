from django.contrib import admin
from django.urls import (path, include)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('rest_api.urls')),
    path(r'', include('soap_api.urls')),
    path(r'get_auth_token', obtain_auth_token, name='get_auth_token')
]
