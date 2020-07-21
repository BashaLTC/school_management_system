import lxml.etree as ET
from xmltodict import parse as xml_to_dict_parse
from dicttoxml import dicttoxml
from django.views import View

from rest_framework import status
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.files.temp import NamedTemporaryFile

from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from school_management_system.settings import MAX_QUERY_RESULT_LIMIT
from rest_api.serializers import (StudentDetailsSerializer, TeacherDetailsSerializer, ParentsDetailsSerializer, DriverDetailsSerializer)
from rest_api.models import (StudentDetails, TeacherDetails, ParentsDetails, DriverDetails)


class CreateStudent(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self, request):

        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        student_serializer = StudentDetailsSerializer(data=xml_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchStudent(APIView):
    """
    ?name=<value>
    """

    def get(self, request):
        student_details = StudentDetails.objects.all()[:MAX_QUERY_RESULT_LIMIT].values()
        data = request.body.decode('utf-8')
        if data:
            xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
            name = xml_data.get('name', None)
            if name is not None:
                student_details = StudentDetails.objects.filter(student_name__icontains=name)[:MAX_QUERY_RESULT_LIMIT].values()

        student_details = [i for i in student_details]
        dict_xml_data = dicttoxml(student_details).decode('utf-8')
        file_name = NamedTemporaryFile(delete=True)
        with open(file_name.name, 'w') as f:
            f.write(dict_xml_data)
        print(file_name.name)

        return HttpResponse(open(file_name.name).read(), content_type='text/xml')


class DeleteStudent(APIView):

    def delete(self, request):

        name = request.query_params.get('name', None)
        if name:
            delete_value = StudentDetails.objects.filter(student_name=name).delete()
            if delete_value[0]:
                return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


class CreateParent(APIView):

    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        parent_serializer = ParentsDetailsSerializer(data=xml_data)
        if parent_serializer.is_valid():
            parent_serializer.save()
            return JsonResponse(parent_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(parent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchParent(APIView):
    """
    ?name=<value>
    """

    def get(self, request):
        tutorials = ParentsDetails.objects.all()[:MAX_QUERY_RESULT_LIMIT].values()
        name = request.query_params.get('name', None)
        if name is not None:
            tutorials = ParentsDetails.objects.filter(student_name__icontains=name)

        tutorials_serializer = ParentsDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


class DeleteParent(APIView):

    def delete(self, request):

        name = request.query_params.get('name', None)
        if name:
            delete_value = ParentsDetails.objects.filter(parent_name=name).delete()
            if delete_value[0]:
                return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


class CreateTeacher(APIView):

    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        teacher_serializer = TeacherDetailsSerializer(data=xml_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse(teacher_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchTeacher(APIView):

    def get(self, request):

        tutorials = TeacherDetails.objects.all()
        name = request.query_params.get('name', None)
        if name is not None:
            tutorials = TeacherDetails.objects.filter(student_name__icontains=name)

        tutorials_serializer = TeacherDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


class DeleteTeacher(APIView):

    def delete(self, request):

        name = request.query_params.get('name', None)
        if name:
            delete_value = TeacherDetails.objects.filter(teacher_name=name).delete()
            if delete_value[0]:
                return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


class CreateDriver(APIView):

    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        driver_serializer = DriverDetailsSerializer(data=xml_data)
        if driver_serializer.is_valid():
            driver_serializer.save()
            return JsonResponse(driver_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(driver_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchDriver(APIView):

    def get(self, request):

        tutorials = DriverDetails.objects.all()
        name = request.query_params.get('name', None)
        if name is not None:
            tutorials = DriverDetails.objects.filter(student_name__icontains=name)

        tutorials_serializer = DriverDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


class DeleteDriver(APIView):

    def delete(self, request):

        name = request.query_params.get('name', None)
        if name:
            delete_value = DriverDetails.objects.filter(driver_name=name).delete()
            if delete_value[0]:
                return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
