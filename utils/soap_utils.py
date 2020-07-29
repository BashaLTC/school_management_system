from spyne.server.django import DjangoView
from spyne.protocol.soap import Soap11
from school_management_system.config import API_NAME


def register_the_view_in_soap(class_name):
    return DjangoView.as_view(
        services=[class_name],
        tns=API_NAME,
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11())
