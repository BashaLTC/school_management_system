# from django.urls import path
# from soap_api.views import my_soap_application
#
# urlpatterns = [
#     path(r'soap_service/', my_soap_application),
# ]

from django.urls import path
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView

from soap_api.views import (hello_app, application, HelloWorldService)

urlpatterns = [
    path(r'hello_world/', hello_app),
    path(r'say_hello/', DjangoView.as_view(
        services=[HelloWorldService],
        tns='spyne.exmaple.hello',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11()
    )),
    path(r'api/', DjangoView.as_view(application=application)),
]
