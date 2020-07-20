from rest_framework import serializers
from rest_api.models import (StudentDetails, ParentsDetails, TeacherDetails, DriverDetails)


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = tuple(i.name for i in StudentDetails._meta.fields)


class ParentsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentsDetails
        fields = tuple(i.name for i in ParentsDetails._meta.fields)


class TeacherDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherDetails
        fields = tuple(i.name for i in TeacherDetails._meta.fields)


class DriverDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverDetails
        fields = tuple(i.name for i in DriverDetails._meta.fields)
