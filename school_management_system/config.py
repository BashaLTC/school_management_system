from school_management_system.settings import BASE_DIR

MAX_QUERY_RESULT_LIMIT = 50
XML_LOCATION = BASE_DIR + '/utils/xml_responses/'

REST_MIDDLEWARE_CONFIG = {

    201: {'Status': 'Created', 'description': 'A new resource was successfully created.'},
    400: {'Status': 'Bad Request', 'description': 'The request was invalid.'},
    401: {'Status': 'Unauthorized', 'description': 'The request did not include an authentication token or the authentication token was expired.'},
    403: {'Status': 'Forbidden', 'description': 'The client did not have permission to access the requested resource.'},
    404: {'Status': 'Not Found', 'description': 'The requested resource was not found.'},
    405: {'Status': 'Method Not Allowed',
          'description': 'The HTTP method in the request was not supported by the resource. For example, the DELETE method cannot be used with the Agent API.'},
    409: {'Status': 'Conflict',
          'description': 'The request could not be completed due to a conflict. For example,  POST ContentStore Folder API cannot complete if the given file or folder name '
                         'already exists in the parent location.'},
    500: {'Status': 'Internal Server Error', 'description': 'The request was not completed due to an internal error on the server side.'},
    503: {'Status': 'Service Unavailable', 'description': 'The server was unavailable.'},

}
