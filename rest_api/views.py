from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (authentication_classes, permission_classes)

from rest_api.serializers import (StudentDetailsSerializer, TeacherDetailsSerializer, ParentsDetailsSerializer, DriverDetailsSerializer)
from rest_api.models import (StudentDetails, TeacherDetails, ParentsDetails, DriverDetails)
from utils.util import compose_into_a_single_decorator


not_use_token_as_default_auth = compose_into_a_single_decorator(authentication_classes([]), permission_classes([]))


class CreateStudent(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = JSONParser().parse(request)
        tutorial_serializer = StudentDetailsSerializer(data=data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return self.post(request)


class SearchStudent(APIView):
    """
    ?name=<value>
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tutorials = StudentDetails.objects.all()

        name = request.query_params.get('name', None)
        if name is not None:
            tutorials = StudentDetails.objects.filter(student_name__icontains=name)

        tutorials_serializer = StudentDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


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
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ParentsDetailsSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return self.post(request)


class SearchParent(APIView):

    def get(self, request):

        tutorials = ParentsDetails.objects.all()
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
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TeacherDetailsSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return self.post(request)


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


@not_use_token_as_default_auth
class CreateDriver(APIView):

    def post(self, request, *args, **kwargs):
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = DriverDetailsSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return self.post(request)


@not_use_token_as_default_auth
class SearchDriver(APIView):

    def get(self, request):

        tutorials = DriverDetails.objects.all()
        name = request.query_params.get('name', None)
        if name is not None:
            tutorials = DriverDetails.objects.filter(student_name__icontains=name)

        tutorials_serializer = DriverDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


@not_use_token_as_default_auth
class DeleteDriver(APIView):

    def delete(self, request):

        name = request.query_params.get('name', None)
        if name:
            delete_value = DriverDetails.objects.filter(driver_name=name).delete()
            if delete_value[0]:
                return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
