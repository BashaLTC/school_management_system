# from django.views.decorators.csrf import csrf_exempt
# from spyne.application import Application
# from spyne.decorator import rpc
# from spyne.model.primitive import Unicode, Integer
# from spyne.protocol.soap import Soap11
# from spyne.server.django import DjangoApplication
# from spyne.service import ServiceBase
#
#
# class SoapService(ServiceBase):
#
#     @rpc(Unicode(nillable=False), _return=Unicode)
#     def hello(ctx, name):
#         return f'Hello, {name}'
#
#     @rpc(Integer(nillable=False), Integer(nillable=False), _return=Integer)
#     def sum(ctx, a, b):
#         return int(a + b)
#
#
# soap_app = Application(
#     [SoapService],
#     tns='django.soap.exmaple',
#     in_protocol=Soap11(validator='lxml'),
#     out_protocol=Soap11(),
# )
#
# django_soap_application = DjangoApplication(soap_app)
# my_soap_application = csrf_exempt(django_soap_application)

import logging
from spyne import (Application, rpc, ServiceBase, Integer, Unicode)
from spyne import Iterable
from spyne.protocol.http import HttpRpc
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from django.views.decorators.csrf import csrf_exempt

logging.basicConfig(level=logging.DEBUG)


class HelloWorldService(ServiceBase):

    @rpc(Unicode, Integer)
    def say_hello(ctx, name, times):
        for i in range(name):
            yield 'Hello, %s' % name


application = Application(
    [HelloWorldService],
    tns='spyne.example.hello',
    in_protocol=HttpRpc(validator='soft'),
    out_protocol=Soap11()
)

hello_app = csrf_exempt(DjangoApplication(application))
