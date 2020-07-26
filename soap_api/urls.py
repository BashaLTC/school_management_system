from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from rest_framework.urlpatterns import format_suffix_patterns
from soap_api.views import (CreateStudent, SearchStudent, DeleteStudent, CreateParent, SearchParent, DeleteParent, CreateTeacher, SearchTeacher, DeleteTeacher,
                            CreateDriver, SearchDriver, DeleteDriver)

urlpatterns = [
    # Student endpoints
    path(r'soap_api/create_student', never_cache(csrf_exempt(CreateStudent.as_view()))),
    path(r'soap_api/search_student', never_cache(csrf_exempt(SearchStudent.as_view()))),
    path(r'soap_api/delete_student', never_cache(csrf_exempt(DeleteStudent.as_view()))),

    # Parent endpoints
    path(r'soap_api/create_parent', never_cache(csrf_exempt(CreateParent.as_view()))),
    path(r'soap_api/search_parent', never_cache(csrf_exempt(SearchParent.as_view()))),
    path(r'soap_api/delete_parent', never_cache(csrf_exempt(DeleteParent.as_view()))),

    # Teacher endpoints
    path(r'soap_api/create_teacher', never_cache(csrf_exempt(CreateTeacher.as_view()))),
    path(r'soap_api/search_teacher', never_cache(csrf_exempt(SearchTeacher.as_view()))),
    path(r'soap_api/delete_teacher', never_cache(csrf_exempt(DeleteTeacher.as_view()))),

    # Driver endpoints
    path(r'soap_api/create_driver', never_cache(csrf_exempt(CreateDriver.as_view()))),
    path(r'soap_api/search_driver', never_cache(csrf_exempt(SearchDriver.as_view()))),
    path(r'soap_api/delete_driver', never_cache(csrf_exempt(DeleteDriver.as_view()))),
]

urlpatterns = format_suffix_patterns(urlpatterns)
