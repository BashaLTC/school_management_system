from django.urls import path
from django.views.decorators.cache import never_cache
from spyne.server.django import DjangoView
from spyne.protocol.soap import Soap11
from school_management_system.config import API_NAME
from utils.soap_utils import register_the_view_in_soap
from soap_api.views import (SearchStudent, DeleteStudent, SearchParent, DeleteParent, SearchTeacher, DeleteTeacher, SearchDriver, DeleteDriver, CreateDriver, CreateStudent,
                            CreateParent, CreateTeacher)

urlpatterns = [
    # student
    path(r'soap_api/create_student/', never_cache(register_the_view_in_soap(CreateStudent))),
    path(r'soap_api/search_student/', never_cache(register_the_view_in_soap(SearchStudent))),
    path(r'soap_api/delete_student/', never_cache(register_the_view_in_soap(DeleteStudent))),

    # parent
    path(r'soap_api/create_parent/', register_the_view_in_soap(CreateParent)),
    path(r'soap_api/search_parent/', register_the_view_in_soap(SearchParent)),
    path(r'soap_api/delete_parent/', register_the_view_in_soap(DeleteParent)),

    # teacher
    path(r'soap_api/create_teacher/', register_the_view_in_soap(CreateTeacher)),
    path(r'soap_api/search_teacher/', register_the_view_in_soap(SearchTeacher)),
    path(r'soap_api/delete_teacher/', register_the_view_in_soap(DeleteTeacher)),

    # driver
    path(r'soap_api/create_driver/', register_the_view_in_soap(CreateDriver)),
    path(r'soap_api/delete_driver/', register_the_view_in_soap(DeleteDriver)),
    path(r'soap_api/search_driver/', register_the_view_in_soap(SearchDriver)),

    path(r'soap_api/', DjangoView.as_view(
        services=[CreateStudent, SearchStudent, DeleteStudent, CreateParent, SearchParent, DeleteParent, CreateTeacher, SearchTeacher, DeleteTeacher, CreateDriver, DeleteDriver,
                  SearchDriver],
        tns=API_NAME,
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11())),
]
