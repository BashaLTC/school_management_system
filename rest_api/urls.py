from django.urls import (path, re_path)
from rest_api.views import (CreateStudent, SearchStudent, DeleteStudent, CreateParent, SearchParent, DeleteParent, CreateTeacher, SearchTeacher, DeleteTeacher, CreateDriver,
                            SearchDriver, DeleteDriver)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Student endpoints
    path(r'rest_api/create_student', CreateStudent.as_view()),
    path(r'rest_api/search_student', SearchStudent.as_view()),
    path(r'rest_api/delete_student', DeleteStudent.as_view()),

    # Parent endpoints
    path(r'rest_api/create_parent', CreateParent.as_view()),
    path(r'rest_api/search_parent', SearchParent.as_view()),
    path(r'rest_api/delete_parent', DeleteParent.as_view()),

    # Teacher endpoints
    path(r'rest_api/create_teacher', CreateTeacher.as_view()),
    path(r'rest_api/search_teacher', SearchTeacher.as_view()),
    path(r'rest_api/delete_teacher', DeleteTeacher.as_view()),

    # Driver endpoints
    path(r'rest_api/create_driver', CreateDriver.as_view()),
    path(r'rest_api/search_driver', SearchDriver.as_view()),
    path(r'rest_api/delete_driver', DeleteDriver.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
