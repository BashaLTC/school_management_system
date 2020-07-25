import json
import base64
from django.views import View
from rest_framework import status
from rest_framework import routers
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_api.serializers import UserSerializers
from django.http.response import JsonResponse
from rest_framework_api_key.models import APIKey
from django.utils.timezone import now
from datetime import timedelta

from school_management_system.config import API_KEY_EXPIRY_HOURS


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


router = routers.DefaultRouter()
router.register('User', UserViewSets, basename='user_api')


def authenticate_user(request):
    auth_header = request.META['HTTP_AUTHORIZATION']
    encoded_credentials = auth_header.split(' ')[1]  # Removes "Basic " to isolate credentials
    decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
    username = decoded_credentials[0]
    password = decoded_credentials[1]
    return authenticate(username=username, password=password)


class ApiTokenGenerator(View):

    def post(self, request):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        if data:
            if authenticate(username=data.get('username'), password=data.get('password')):
                api_key, key = APIKey.objects.create_key(name=data['username'], expiry_date=now() + timedelta(hours=API_KEY_EXPIRY_HOURS))
                return JsonResponse({"API_KEY_NAME": api_key.name, 'API_KEY': key, "API_KEY_EXPIRY": api_key.expiry_date})
            return JsonResponse({'error': True}, status=status.HTTP_401_UNAUTHORIZED)
        return JsonResponse({'error': True}, status=status.HTTP_204_NO_CONTENT)
