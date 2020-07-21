from django.urls import (path, re_path)
from django.views.decorators.csrf import csrf_exempt
from soap_api.views import (CreateStudent, SearchStudent, DeleteStudent, CreateParent, SearchParent, DeleteParent, CreateTeacher, SearchTeacher, DeleteTeacher, CreateDriver,
                            SearchDriver, DeleteDriver)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Student endpoints
    path(r'soap_api/create_student', csrf_exempt(CreateStudent.as_view())),
    path(r'soap_api/search_student', csrf_exempt(SearchStudent.as_view())),
    path(r'soap_api/delete_student', csrf_exempt(DeleteStudent.as_view())),

    # Parent endpoints
    path(r'soap_api/create_parent', csrf_exempt(CreateParent.as_view())),
    path(r'soap_api/search_parent', csrf_exempt(SearchParent.as_view())),
    path(r'soap_api/delete_parent', csrf_exempt(DeleteParent.as_view())),

    # Teacher endpoints
    path(r'soap_api/create_teacher', csrf_exempt(CreateTeacher.as_view())),
    path(r'soap_api/search_teacher', csrf_exempt(SearchTeacher.as_view())),
    path(r'soap_api/delete_teacher', csrf_exempt(DeleteTeacher.as_view())),

    # Driver endpoints
    path(r'soap_api/create_driver', csrf_exempt(CreateDriver.as_view())),
    path(r'soap_api/search_driver', csrf_exempt(SearchDriver.as_view())),
    path(r'soap_api/delete_driver', csrf_exempt(DeleteDriver.as_view())),
]

urlpatterns = format_suffix_patterns(urlpatterns)
