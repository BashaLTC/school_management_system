### REST API
    * API  1 - endpoint : createStudent HTTP Method: PUT/POST  -> Bearer token based auth (key is valida forever)
    * API- 2 - endpoint : searchStudent HTTP Method: GET
    * API- 3 - endpoint : deleteStudent HTTP Method: DELETE
    
    
    * API  4 - endpoint : createParent HTTP Method: PUT/POST -> Basic Auth :username: :password: 
    * API- 5 - endpoint : searchParent HTTP Method: GET
    * API- 6 - endpoint : deleteParent HTTP Method: DELETE
    
    
    * API  7 - endpoint : createTeacher HTTP Method: PUT/POST  -> API KEY  (key is valida for a single day)
    * API- 8 - endpoint : searchTeacher HTTP Method: GET
    * API- 9 - endpoint : deleteTeacher HTTP Method: DELETE
    
    
    * API-10 - endpoint : createDriver HTTP Method: PUT/POST  ->  NO AUTH 
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

### setup

1. MySql setup
    
   ```text

     CREATE USER 'liberty'@'localhost' IDENTIFIED BY 'liberty123';

     GRANT ALL ON *.* TO 'liberty'@'localhost';

     mysql -uliberty -pliberty123

     CREATE DATABASE school_db
      ```   
2. copy the data from the below mentioned file in the next mentioned files and locations
    
    ```shell script
   
    school_management_system/external/uwsgi.conf  -->  /etc/systemd/system/uwsgi.service
    
    school_management_system/external/school_management_system.ini  -->   /etc/uwsgi/sites/school_management_system.ini
   
    
    ```
    Add the content of this file into the http block and we are running the port 80 which is http. 
    ```shell script
     school_management_system/external/nginx.conf  -->   /etc/uwsgi/sites/nginx.conf
    ```
   
3. Need to create the super user accounts currently the only one in the db is 
    
   ```json
     {"username": "deesh","password": "deesh"}
    ```
    