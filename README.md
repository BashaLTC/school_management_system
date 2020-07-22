### REST API
* API  1 - endpoint : createStudent HTTP Method: PUT/POST
* API- 2 - endpoint : searchStudent HTTP Method: GET
* API- 3 - endpoint : deleteStudent HTTP Method: DELETE

* API  4 - endpoint : createParent HTTP Method: PUT/POST
* API- 5 - endpoint : searchParent HTTP Method: GET
* API- 6 - endpoint : deleteParent HTTP Method: DELETE

* API  7 - endpoint : createTeacher HTTP Method: PUT/POST
* API- 8 - endpoint : searchTeacher HTTP Method: GET
* API- 9 - endpoint : deleteTeacher HTTP Method: DELETE

* API-10 - endpoint : createDriver HTTP Method: PUT/POST
* API-11 - endpoint : searchDriver HTTP Method: GET
* API-12 - endpoint : deleteDriver HTTP Method: DELETE


### AUTH MEHODS.

1. TOKEN BASED AUTHENTICATION
    * Need to pass a token to authenticate the request.
        pass
        
    * To get the token need to call the below mentioned end point with the body as the following json
        
        `http://localhost:8000/get_auth_token`
          
        ```json
        {
            "username": "deesh",
            "password": "deesh"
        }
        ```
    * Once you get the TOKEN you need to pass the token for each request else it will be considered as the unauthorized 
       `401`
       
       ```json
        {"Authorization": "Token <token we got from the previous step>"}
```