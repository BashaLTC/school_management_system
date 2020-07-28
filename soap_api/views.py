import logging

from spyne import (Application, rpc, ServiceBase, Integer, Unicode)
from spyne import (Iterable, AnyDict)
from spyne.protocol.http import HttpRpc
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from rest_api.models import (StudentDetails, TeacherDetails, ParentsDetails, DriverDetails)
from school_management_system.config import MAX_QUERY_RESULT_LIMIT
from school_management_system.authentications import (soap_authenticate, soap_authenticate_api_key, soap_token_authenticated)
from rest_api.serializers import (StudentDetailsSerializer, TeacherDetailsSerializer, ParentsDetailsSerializer, DriverDetailsSerializer)

# logging.basicConfig(level=logging.DEBUG)


class CreateStudent(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, _returns=Iterable(AnyDict))
    def create_student(ctx, token, student_name, age, class_name, section, blood_group, parent_name, parent_phone_number, class_teacher, favourite_sport, favourite_subject):
        if soap_token_authenticated(token):
            data = dict(
                student_name=student_name,
                age=age,
                class_name=class_name,
                section=section,
                blood_group=blood_group,
                parent_name=parent_name,
                parent_phone_number=parent_phone_number,
                class_teacher=class_teacher,
                favourite_sport=favourite_sport,
                favourite_subject=favourite_subject,
            )
            tutorial_serializer = StudentDetailsSerializer(data=data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return [{"Status": 'OK'}]
            return [tutorial_serializer.errors]
        return [{'token': "invalid"}]


class SearchStudent(ServiceBase):

    @rpc(Unicode, Unicode, _returns=Iterable(AnyDict))
    def search_student(ctx, token, name):
        if soap_token_authenticated(token):
            if name:
                data = StudentDetails.objects.filter(student_name=name).values()
                if data:
                    return [{i: j} for i, j in data[0].items()]
            return []
        return [{'token': "invalid"}]


class DeleteStudent(ServiceBase):

    @rpc(Unicode, Unicode, _returns=Iterable(AnyDict))
    def delete_student(ctx, token, name):
        if soap_token_authenticated(token):
            if name:
                delete_value = StudentDetails.objects.filter(student_name=name).delete()
                if delete_value[0]:
                    return [{'deleted': True}]
            return []
        return [{'token': "invalid"}]


class CreateParent(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, _returns=Iterable(AnyDict))
    def create_parent(ctx, username, password, parent_name, student_name, age, blood_group, educational_qualification, address, phone_number):
        if soap_authenticate(username=username, password=password):
            data = dict(
                parent_name=parent_name,
                student_name=student_name,
                age=age,
                blood_group=blood_group,
                educational_qualification=educational_qualification,
                address=address,
                phone_number=phone_number,
            )
            tutorial_serializer = ParentsDetailsSerializer(data=data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return [{"Status": 'OK'}]
            return [tutorial_serializer.errors]
        return [{'credentials': "invalid"}]


class SearchParent(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, _returns=Iterable(AnyDict))
    def search_teacher(ctx, username, password, name):
        if soap_authenticate(username=username, password=password):
            if name:
                data = ParentsDetails.objects.filter(parent_name=name).values()
                if data:
                    return [{i: j} for i, j in data[0].items()]
                return []
        return [{'credentials': "invalid"}]


class DeleteParent(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, _returns=Iterable(AnyDict))
    def delete_teacher(ctx, username, password, name):
        if soap_authenticate(username=username, password=password):
            if name:
                delete_value = ParentsDetails.objects.filter(parent_name=name).delete()
                if delete_value[0]:
                    return [{'deleted': True}]
            return []
        return [{'credentials': "invalid"}]


class CreateTeacher(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, _returns=Iterable(AnyDict))
    def create_driver(ctx, api_key, teacher_name, age, phone_number, address, head_of_class, subject, years_of_experience, educational_qualification, complaints):
        if soap_authenticate_api_key(api_key):
            data = dict(
                teacher_name=teacher_name,
                age=age,
                phone_number=phone_number,
                address=address,
                head_of_class=head_of_class,
                subject=subject,
                years_of_experience=years_of_experience,
                educational_qualification=educational_qualification,
                complaints=complaints,
            )
            tutorial_serializer = TeacherDetailsSerializer(data=data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return [{"Status": 'OK'}]
            return [tutorial_serializer.errors]
        return [{'key': "invalid"}]


class SearchTeacher(ServiceBase):

    @rpc(Unicode, Unicode, _returns=Iterable(AnyDict))
    def search_teacher(ctx, api_key, name):
        if soap_authenticate_api_key(api_key):
            if name:
                data = TeacherDetails.objects.filter(teacher_name=name).values()
                if data:
                    return [{i: j} for i, j in data[0].items()]
                return []
        return [{'key': "invalid"}]


class DeleteTeacher(ServiceBase):

    @rpc(Unicode, Unicode, _returns=Iterable(AnyDict))
    def delete_teacher(ctx, api_key, name):
        if soap_authenticate_api_key(api_key):
            if name:
                delete_value = TeacherDetails.objects.filter(teacher_name=name).delete()
                if delete_value[0]:
                    return [{'deleted': True}]
            return []
        return [{'key': "invalid"}]


class CreateDriver(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, _returns=Iterable(AnyDict))
    def create_driver(ctx, driver_name, age, phone_number, address, lic_no, experience, complaints, route):
        data = dict(
            driver_name=driver_name,
            age=age,
            phone_number=phone_number,
            address=address,
            lic_no=lic_no,
            experience=experience,
            complaints=complaints,
            route=route,
        )
        tutorial_serializer = DriverDetailsSerializer(data=data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return [{"Status": 'OK'}]
        return [tutorial_serializer.errors]


class SearchDriver(ServiceBase):

    @rpc(Unicode, _returns=Iterable(AnyDict))
    def search_driver(ctx, name=None):
        if name:
            data = DriverDetails.objects.filter(driver_name=name).values()
            if data:
                return [{i: j} for i, j in data[0].items()]
            return []


class DeleteDriver(ServiceBase):

    @rpc(Unicode, _returns=Iterable(AnyDict))
    def delete_driver(ctx, name=None):
        if name:
            delete_value = DriverDetails.objects.filter(driver_name=name).delete()
            if delete_value[0]:
                return [{'deleted': True}]
        return []


