from django.views import View
from rest_framework import status
from spyne import (Iterable, AnyDict)
from spyne import (rpc, ServiceBase, Unicode)
from django.http.response import HttpResponse

from school_management_system.config import GIF_LOCATION
from rest_api.models import (StudentDetails, TeacherDetails, ParentsDetails, DriverDetails)
from school_management_system.authentications import (soap_authenticate, soap_authenticate_api_key, soap_token_authenticated)
from rest_api.serializers import (StudentDetailsSerializer, TeacherDetailsSerializer, ParentsDetailsSerializer, DriverDetailsSerializer)


class CreateStudent(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, _returns=Iterable(AnyDict))
    def create_student(ctx, student_name, age, class_name, section, blood_group, parent_name, parent_phone_number, class_teacher, favourite_sport, favourite_subject):
        if soap_token_authenticated(ctx):
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

    @rpc(Unicode, _returns=Iterable(AnyDict))
    def search_student(ctx, name):
        if soap_token_authenticated(ctx):
            if name:
                data = StudentDetails.objects.filter(student_name=name).values()
                if data:
                    return [{i: j} for i, j in data[0].items()]
            return [{"status": 'No Data Found'}]
        return [{'token': "invalid"}]


class DeleteStudent(ServiceBase):

    @rpc(Unicode, _returns=Iterable(AnyDict))
    def delete_student(ctx, name):
        if soap_token_authenticated(ctx):
            if name:
                delete_value = StudentDetails.objects.filter(student_name=name).delete()
                if delete_value[0]:
                    return [{'deleted': True}]
            return [{"status": 'No Data Found'}]
        return [{'token': "invalid"}]


class CreateParent(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, _returns=Iterable(AnyDict))
    def create_parent(ctx, parent_name, student_name, age, blood_group, educational_qualification, address, phone_number):
        if soap_authenticate(ctx):
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

    @rpc(Unicode, _returns=Iterable(AnyDict))
    def search_parent(ctx, name):
        if soap_authenticate(ctx):
            if name:
                data = ParentsDetails.objects.filter(parent_name=name).values()
                if data:
                    return [{i: j} for i, j in data[0].items()]
                return [{"status": 'No Data Found'}]
        return [{'credentials': "invalid"}]


class DeleteParent(ServiceBase):

    @rpc(Unicode, _returns=Iterable(AnyDict))
    def delete_parent(ctx, name):
        if soap_authenticate(ctx):
            if name:
                delete_value = ParentsDetails.objects.filter(parent_name=name).delete()
                if delete_value[0]:
                    return [{'deleted': True}]
            return [{"status": 'No Data Found'}]
        return [{'credentials': "invalid"}]


class CreateTeacher(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, _returns=Iterable(AnyDict))
    def create_teacher(ctx, teacher_name, age, phone_number, address, head_of_class, subject, years_of_experience, educational_qualification, complaints):
        if soap_authenticate_api_key(ctx):
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

    @rpc(Unicode, _returns=Iterable(AnyDict))
    def search_teacher(ctx, name):
        if soap_authenticate_api_key(ctx):
            if name:
                data = TeacherDetails.objects.filter(teacher_name=name).values()
                if data:
                    return [{i: j} for i, j in data[0].items()]
                return [{"status": 'No Data Found'}]
        return [{'key': "invalid"}]


class DeleteTeacher(ServiceBase):

    @rpc(Unicode, _returns=Iterable(AnyDict))
    def delete_teacher(ctx, name):
        if soap_authenticate_api_key(ctx):
            if name:
                delete_value = TeacherDetails.objects.filter(teacher_name=name).delete()
                if delete_value[0]:
                    return [{'deleted': True}]
            return [{"status": 'No Data Found'}]
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
        return [{"status": 'No Data Found'}]


class HomeView(View):
    def get(self, request):
        image_data = open(GIF_LOCATION + '404_page_not_found.gif', "rb").read()
        return HttpResponse(image_data, content_type="image/png", status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        return self.get(request)

    def put(self, request):
        return self.get(request)

    def delete(self, request):
        return self.get(request)


class PingPong(View):

    def get(self, request):
        return HttpResponse("Pong")

    def post(self, request):
        return self.get(request)

    def put(self, request):
        return self.get(request)

    def delete(self, request):
        return self.get(request)