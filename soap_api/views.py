
from django.views import View
from dicttoxml import dicttoxml
from rest_framework import status
from xmltodict import parse as xml_to_dict_parse
from django.core.files.temp import NamedTemporaryFile
from django.http.response import JsonResponse, HttpResponse

from utils.util import decide_the_message
from school_management_system.settings import (MAX_QUERY_RESULT_LIMIT, XML_LOCATION)
from rest_api.models import (StudentDetails, TeacherDetails, ParentsDetails, DriverDetails)
from rest_api.serializers import (StudentDetailsSerializer, TeacherDetailsSerializer, ParentsDetailsSerializer, DriverDetailsSerializer)


class CreateStudent(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        student_serializer = StudentDetailsSerializer(data=xml_data)
        if student_serializer.is_valid():
            student_serializer.save()
            success_message = decide_the_message(student_serializer.data, open(XML_LOCATION + 'created.xml').read())
            return HttpResponse(success_message, status=status.HTTP_201_CREATED)
        error_message = decide_the_message(student_serializer.errors, open(XML_LOCATION + 'not_created.xml').read())
        return HttpResponse(error_message, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        student_serializer = StudentDetailsSerializer(data=xml_data)
        if student_serializer.is_valid():
            student_serializer.save()
            success_message = decide_the_message(student_serializer.data, open(XML_LOCATION + 'created.xml').read())
            return HttpResponse(success_message, status=status.HTTP_201_CREATED)
        error_message = decide_the_message(student_serializer.errors, open(XML_LOCATION + 'not_created.xml').read())
        return HttpResponse(error_message, status=status.HTTP_400_BAD_REQUEST)


class SearchStudent(View):
    """
    ?name=<value>
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

        return HttpResponse(open(file_name.name).read(), content_type='text/xml')


class DeleteStudent(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self, request):
        data = request.body.decode('utf-8')
        if data:
            xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
            name = xml_data.get('name', None)
            if name is not None:
                delete_value = StudentDetails.objects.filter(student_name=name).delete()
                if delete_value[0]:
                    return HttpResponse(open(XML_LOCATION + 'deleted.xml').read(), content_type='text/xml', status=status.HTTP_204_NO_CONTENT)
        return HttpResponse(open(XML_LOCATION + 'not_deleted.xml').read(), content_type='text/xml', status=status.HTTP_400_BAD_REQUEST)


class CreateParent(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        parent_serializer = ParentsDetailsSerializer(data=xml_data)
        if parent_serializer.is_valid():
            parent_serializer.save()
            success_message = decide_the_message(parent_serializer.data, open(XML_LOCATION + 'created.xml').read())
            return HttpResponse(success_message, status=status.HTTP_201_CREATED)
        error_message = decide_the_message(parent_serializer.errors, open(XML_LOCATION + 'not_created.xml').read())
        return HttpResponse(error_message, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        parent_serializer = ParentsDetailsSerializer(data=xml_data)
        if parent_serializer.is_valid():
            parent_serializer.save()
            success_message = decide_the_message(parent_serializer.data, open(XML_LOCATION + 'created.xml').read())
            return HttpResponse(success_message, status=status.HTTP_201_CREATED)
        error_message = decide_the_message(parent_serializer.errors, open(XML_LOCATION + 'not_created.xml').read())
        return HttpResponse(error_message, status=status.HTTP_400_BAD_REQUEST)


class SearchParent(View):
    """
    ?name=<value>
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request):
        parent_details = ParentsDetails.objects.all()[:MAX_QUERY_RESULT_LIMIT].values()
        data = request.body.decode('utf-8')
        if data:
            xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
            name = xml_data.get('name', None)
            if name is not None:
                parent_details = ParentsDetails.objects.filter(parent_name__icontains=name)[:MAX_QUERY_RESULT_LIMIT].values()
        parent_details = [i for i in parent_details]
        dict_xml_data = dicttoxml(parent_details).decode('utf-8')
        file_name = NamedTemporaryFile(delete=True)
        with open(file_name.name, 'w') as f:
            f.write(dict_xml_data)
        return HttpResponse(open(file_name.name).read(), content_type='text/xml')


class DeleteParent(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self, request):
        data = request.body.decode('utf-8')
        if data:
            xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
            name = xml_data.get('name', None)
            if name is not None:
                delete_value = ParentsDetails.objects.filter(parent_name=name).delete()
                if delete_value[0]:
                    return HttpResponse(open(XML_LOCATION + 'deleted.xml').read(), content_type='text/xml', status=status.HTTP_204_NO_CONTENT)
        return HttpResponse(open(XML_LOCATION + 'not_deleted.xml').read(), content_type='text/xml', status=status.HTTP_400_BAD_REQUEST)


class CreateTeacher(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        teacher_serializer = TeacherDetailsSerializer(data=xml_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            success_message = decide_the_message(teacher_serializer.data, open(XML_LOCATION + 'created.xml').read())
            return HttpResponse(success_message, status=status.HTTP_201_CREATED)
        error_message = decide_the_message(teacher_serializer.errors, open(XML_LOCATION + 'not_created.xml').read())
        return HttpResponse(error_message, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        teacher_serializer = TeacherDetailsSerializer(data=xml_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            success_message = decide_the_message(teacher_serializer.data, open(XML_LOCATION + 'created.xml').read())
            return HttpResponse(success_message, status=status.HTTP_201_CREATED)
        error_message = decide_the_message(teacher_serializer.errors, open(XML_LOCATION + 'not_created.xml').read())
        return HttpResponse(error_message, status=status.HTTP_400_BAD_REQUEST)


class SearchTeacher(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request):
        teacher_details = TeacherDetails.objects.all()[:MAX_QUERY_RESULT_LIMIT].values()
        data = request.body.decode('utf-8')
        if data:
            xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
            name = xml_data.get('name', None)
            if name is not None:
                teacher_details = TeacherDetails.objects.filter(teacher_name__icontains=name)[:MAX_QUERY_RESULT_LIMIT].values()
        teacher_details = [i for i in teacher_details]
        dict_xml_data = dicttoxml(teacher_details).decode('utf-8')
        file_name = NamedTemporaryFile(delete=True)
        with open(file_name.name, 'w') as f:
            f.write(dict_xml_data)
        return HttpResponse(open(file_name.name).read(), content_type='text/xml')


class DeleteTeacher(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self, request):
        data = request.body.decode('utf-8')
        if data:
            xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
            name = xml_data.get('name', None)
            if name is not None:
                delete_value = TeacherDetails.objects.filter(teacher_name=name).delete()
                if delete_value[0]:
                    return HttpResponse(open(XML_LOCATION + 'deleted.xml').read(), content_type='text/xml', status=status.HTTP_204_NO_CONTENT)
        return HttpResponse(open(XML_LOCATION + 'not_deleted.xml').read(), content_type='text/xml', status=status.HTTP_400_BAD_REQUEST)


class CreateDriver(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        driver_serializer = DriverDetailsSerializer(data=xml_data)
        if driver_serializer.is_valid():
            driver_serializer.save()
            success_message = decide_the_message(driver_serializer.data, open(XML_LOCATION + 'created.xml').read())
            return HttpResponse(success_message, status=status.HTTP_201_CREATED)
        error_message = decide_the_message(driver_serializer.errors, open(XML_LOCATION + 'not_created.xml').read())
        return HttpResponse(error_message, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.body.decode('utf-8')
        xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
        driver_serializer = DriverDetailsSerializer(data=xml_data)
        if driver_serializer.is_valid():
            driver_serializer.save()
            success_message = decide_the_message(driver_serializer.data, open(XML_LOCATION + 'created.xml').read())
            return HttpResponse(success_message, status=status.HTTP_201_CREATED)
        error_message = decide_the_message(driver_serializer.errors, open(XML_LOCATION + 'not_created.xml').read())
        return HttpResponse(error_message, status=status.HTTP_400_BAD_REQUEST)


class SearchDriver(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request):
        driver_details = DriverDetails.objects.all()[:MAX_QUERY_RESULT_LIMIT].values()
        data = request.body.decode('utf-8')
        if data:
            xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
            name = xml_data.get('name', None)
            if name is not None:
                driver_details = DriverDetails.objects.filter(driver_name__icontains=name)[:MAX_QUERY_RESULT_LIMIT].values()
        driver_details = [i for i in driver_details]
        dict_xml_data = dicttoxml(driver_details).decode('utf-8')
        file_name = NamedTemporaryFile(delete=True)
        with open(file_name.name, 'w') as f:
            f.write(dict_xml_data)
        return HttpResponse(open(file_name.name).read(), content_type='text/xml')


class DeleteDriver(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self, request):
        data = request.body.decode('utf-8')
        if data:
            xml_data = {i: j for i, j in xml_to_dict_parse(data).get('data').items()}
            name = xml_data.get('name', None)
            if name is not None:
                delete_value = DriverDetails.objects.filter(driver_name=name).delete()
                if delete_value[0]:
                    return HttpResponse(open(XML_LOCATION + 'deleted.xml').read(), content_type='text/xml', status=status.HTTP_204_NO_CONTENT)
        return HttpResponse(open(XML_LOCATION + 'not_deleted.xml').read(), content_type='text/xml', status=status.HTTP_400_BAD_REQUEST)
