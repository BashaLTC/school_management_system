from rest_framework import routers
from rest_framework import viewsets
from rest_api.serializers import UserSerializers
from django.contrib.auth.models import User


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


router = routers.DefaultRouter()
router.register('User', UserViewSets, basename='user_api')
