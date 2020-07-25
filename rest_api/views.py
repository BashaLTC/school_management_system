from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (authentication_classes, permission_classes)
from rest_framework_api_key.permissions import HasAPIKey

from utils.util import compose_into_a_single_decorator
from school_management_system.authentications import (authenticate_user, is_token_authenticated, authenticate_api_key)
from rest_api.models import (StudentDetails, TeacherDetails, ParentsDetails, DriverDetails)
from rest_api.serializers import (StudentDetailsSerializer, TeacherDetailsSerializer, ParentsDetailsSerializer, DriverDetailsSerializer)


not_use_token_as_default_auth = compose_into_a_single_decorator(authentication_classes([]), permission_classes([]))


class CreateStudent(APIView):

    def post(self, request):
        if is_token_authenticated(request):
            data = JSONParser().parse(request)
            tutorial_serializer = StudentDetailsSerializer(data=data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'error': 'key is not valid'}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request):
        return self.post(request)


class SearchStudent(APIView):
    """
    ?name=<value>
    """

    def get(self, request):
        if is_token_authenticated(request):
            tutorials = StudentDetails.objects.all()
            name = request.query_params.get('name', None)
            if name is not None:
                tutorials = StudentDetails.objects.filter(student_name__icontains=name)
            tutorials_serializer = StudentDetailsSerializer(tutorials, many=True)
            return JsonResponse(tutorials_serializer.data, safe=False)
        return JsonResponse({'error': 'key is not valid'}, status=status.HTTP_401_UNAUTHORIZED)


class DeleteStudent(APIView):

    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        if is_token_authenticated(request):
            name = request.query_params.get('name', None)
            if name:
                delete_value = StudentDetails.objects.filter(student_name=name).delete()
                if delete_value[0]:
                    return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
                return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'error': 'key is not valid'}, status=status.HTTP_401_UNAUTHORIZED)


class CreateParent(APIView):

    def post(self, request, *args, **kwargs):
        if authenticate_user(request):
            tutorial_data = JSONParser().parse(request)
            tutorial_serializer = ParentsDetailsSerializer(data=tutorial_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'error': True}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request):
        return self.post(request)


class SearchParent(APIView):

    def get(self, request):
        if authenticate_user(request):
            tutorials = ParentsDetails.objects.all()
            name = request.query_params.get('name', None)
            if name is not None:
                tutorials = ParentsDetails.objects.filter(student_name__icontains=name)

            tutorials_serializer = ParentsDetailsSerializer(tutorials, many=True)
            return JsonResponse(tutorials_serializer.data, safe=False)
        return JsonResponse({'error': True}, status=status.HTTP_401_UNAUTHORIZED)


class DeleteParent(APIView):

    def delete(self, request):
        if authenticate_user(request):
            name = request.query_params.get('name', None)
            if name:
                delete_value = ParentsDetails.objects.filter(parent_name=name).delete()
                if delete_value[0]:
                    return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_401_UNAUTHORIZED)


class CreateTeacher(APIView):

    permission_classes = (HasAPIKey,)

    def post(self, request, *args, **kwargs):
        if authenticate_api_key(request):
            tutorial_data = JSONParser().parse(request)
            tutorial_serializer = TeacherDetailsSerializer(data=tutorial_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'error': True}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request):
        return self.post(request)


class SearchTeacher(APIView):

    permission_classes = (HasAPIKey, )

    def get(self, request):
        if authenticate_api_key(request):
            tutorials = TeacherDetails.objects.all()
            name = request.query_params.get('name', None)
            if name is not None:
                tutorials = TeacherDetails.objects.filter(teacher_name__icontains=name)

            tutorials_serializer = TeacherDetailsSerializer(tutorials, many=True)
            return JsonResponse(tutorials_serializer.data, safe=False)
        return JsonResponse({'error': True}, status=status.HTTP_401_UNAUTHORIZED)


class DeleteTeacher(APIView):

    permission_classes = (HasAPIKey,)

    def delete(self, request):
        if authenticate_api_key(request):
            name = request.query_params.get('name', None)
            if name:
                delete_value = TeacherDetails.objects.filter(teacher_name=name).delete()
                if delete_value[0]:
                    return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
                return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'error': True}, status=status.HTTP_401_UNAUTHORIZED)


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


class SearchDriver(APIView):

    def get(self, request, *args, **kwargs):
        tutorials = DriverDetails.objects.all()
        name = request.query_params.get('name', None)
        if name is not None:
            tutorials = DriverDetails.objects.filter(driver_name__icontains=name)

        tutorials_serializer = DriverDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


class DeleteDriver(APIView):

    def delete(self, request, *args, **kwargs):
        name = request.query_params.get('name', None)
        if name:
            delete_value = DriverDetails.objects.filter(driver_name=name).delete()
            if delete_value[0]:
                return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
