from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.cache import never_cache

from rest_api.views import (CreateStudent, SearchStudent, DeleteStudent, CreateParent, SearchParent, DeleteParent, CreateTeacher, SearchTeacher, DeleteTeacher,
                            CreateDriver, SearchDriver, DeleteDriver)

urlpatterns = [
    # Student endpoints
    path(r'rest_api/create_student', never_cache(CreateStudent.as_view())),
    path(r'rest_api/search_student', never_cache(SearchStudent.as_view())),
    path(r'rest_api/delete_student', never_cache(DeleteStudent.as_view())),

    # Parent endpoints
    path(r'rest_api/create_parent', never_cache(CreateParent.as_view())),
    path(r'rest_api/search_parent', never_cache(SearchParent.as_view())),
    path(r'rest_api/delete_parent', never_cache(DeleteParent.as_view())),

    # Teacher endpoints
    path(r'rest_api/create_teacher', never_cache(CreateTeacher.as_view())),
    path(r'rest_api/search_teacher', never_cache(SearchTeacher.as_view())),
    path(r'rest_api/delete_teacher', never_cache(DeleteTeacher.as_view())),

    # Driver endpoints
    path(r'rest_api/create_driver', never_cache(CreateDriver.as_view())),
    path(r'rest_api/search_driver', never_cache(SearchDriver.as_view())),
    path(r'rest_api/delete_driver', never_cache(DeleteDriver.as_view())),
]

urlpatterns = format_suffix_patterns(urlpatterns)
