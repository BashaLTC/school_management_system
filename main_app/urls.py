from django.urls import (path, re_path)
from main_app.views import (CreateStudent, SearchStudent, DeleteStudent, CreateParent, SearchParent, DeleteParent, CreateTeacher, SearchTeacher, DeleteTeacher, CreateDriver,
                            SearchDriver, DeleteDriver)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Student endpoints
    path(r'api/create_student', CreateStudent.as_view()),
    path(r'api/search_student', SearchStudent.as_view()),
    path(r'api/delete_student', DeleteStudent.as_view()),

    # Parent endpoints
    path(r'main_app/create_parent', CreateParent.as_view()),
    path(r'main_app/search_parent', SearchParent.as_view()),
    path(r'main_app/delete_parent', DeleteParent.as_view()),

    # Teacher endpoints
    path(r'main_app/create_teacher', CreateTeacher.as_view()),
    path(r'main_app/search_teacher', SearchTeacher.as_view()),
    path(r'main_app/delete_teacher', DeleteTeacher.as_view()),

    # Driver endpoints
    path(r'main_app/create_driver', CreateDriver.as_view()),
    path(r'main_app/search_driver', SearchDriver.as_view()),
    path(r'main_app/delete_driver', DeleteDriver.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
