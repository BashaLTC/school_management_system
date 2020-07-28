from django.contrib import admin
from django.urls import (path, include)
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from rest_framework.authtoken.views import obtain_auth_token

from soap_api.views_1 import HomeView
from school_management_system.authentications import ApiTokenGenerator

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('rest_api.urls')),
    path(r'', include('soap_api.urls')),
    path(r'get_auth_token', obtain_auth_token, name='get_auth_token'),
    path(r'get_api_token', csrf_exempt(never_cache(ApiTokenGenerator.as_view())), name='get_auth_token'),
    path(r'', csrf_exempt(never_cache(HomeView.as_view())), name=''),
]
