from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from main_app.serializers import (StudentDetailsSerializer, TeacherDetailsSerializer, ParentsDetailsSerializer, DriverDetailsSerializer)
from main_app.models import (StudentDetails, TeacherDetails, ParentsDetails, DriverDetails)


class CreateStudent(APIView):

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        tutorial_serializer = StudentDetailsSerializer(data=data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchStudent(APIView):
    """
    ?name=<value>
    """
    def get(self, request):
        tutorials = StudentDetails.objects.all()

        name = request.query_params.get('name', None)
        if name is not None:
            tutorials = StudentDetails.objects.filter(student_name__icontains=name)

        tutorials_serializer = StudentDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization


class DeleteStudent(APIView):

    def delete(self, request):

        name = request.query_params.get('name', None)
        delete_value = StudentDetails.objects.filter(student_name=name).delete()
        if delete_value[0]:
            return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


class CreateParent(APIView):

    def post(self, request, *args, **kwargs):
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ParentsDetailsSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchParent(APIView):

    def get(self, request):
        tutorials = ParentsDetails.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = ParentsDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


class DeleteParent(APIView):

    def delete(self, request, pk):

        try:
            tutorial = ParentsDetails.objects.get(pk=pk).delete()
            return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except ParentsDetails.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


class CreateTeacher(APIView):

    def post(self, request, *args, **kwargs):
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TeacherDetailsSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchTeacher(APIView):

    def get(self, request):
        tutorials = TeacherDetails.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TeacherDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


class DeleteTeacher(APIView):

    def delete(self, request, pk):

        try:
            tutorial = TeacherDetails.objects.get(pk=pk).delete()
            return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except TeacherDetails.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


class CreateDriver(APIView):

    def post(self, request, *args, **kwargs):
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = StudentDetailsSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchDriver(APIView):

    def get(self, request):
        tutorials = DriverDetails.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = DriverDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


class DeleteDriver(APIView):

    def delete(self, request, pk):

        try:
            tutorial = DriverDetails.objects.get(pk=pk).delete()
            return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except DriverDetails.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
