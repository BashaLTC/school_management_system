from rest_framework import serializers
from django.contrib.auth.models import User

from rest_api.models import (StudentDetails, ParentsDetails, TeacherDetails, DriverDetails)


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'


class ParentsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentsDetails
        fields = '__all__'


class TeacherDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherDetails
        fields = '__all__'


class DriverDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverDetails
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
