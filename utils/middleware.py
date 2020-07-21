from django.shortcuts import HttpResponse
from django.http.response import JsonResponse
from school_management_system.config import (XML_LOCATION, REST_MIDDLEWARE_CONFIG)


class MethodNotAllowedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.get('Content-Type', None) == 'application/json':
            if response.status_code in REST_MIDDLEWARE_CONFIG:
                final_response = REST_MIDDLEWARE_CONFIG.get(response.status_code)
                if response.status_code == 405:
                    final_response.update({'description': f'The HTTP method in the request was not supported by the resource. For example, the {request.method} method '
                                                          f'cannot be used with the Agent API.'})
                return JsonResponse(final_response, safe=False, status=response.status_code)

        elif response.get('Content-Type', 'text/html; charset=utf-8') == 'text/html; charset=utf-8':
            if response.status_code in [401, 403, 404, 405, 409, 500, 5003]:
                return HttpResponse(open(XML_LOCATION + f'{response.status_code}.xml').read(), content_type='text/xml', status=response.status_code)

        return response
