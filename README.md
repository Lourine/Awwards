# Awwards 
#### This is a Python web application using Django  framework and Postgresql,RESTful API.
#### By **[Lourine Millicent](https://github.com/Lourine)**

## Description
This is a web application developed using Django framework, This app allows users to register and Share their projects to be reviewed by other users in terms of Content, Usability and Design.


## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/Lourine/Awwards
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Gallery pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3.8 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python3.8 manage.py makemigrations awwards
 ``` 
 Now Migrate  
 ```bash 
 python3.8 manage.py migrate 
```
##### Run the application  
 ```bash 
 python3.8 manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python3.8 manage.py server 
```
##### Testing the application  
 ```bash 
 python3.8 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.1.2](https://docs.djangoproject.com/en/3.1/)  
* [Heroku](https://heroku.com)  
* [Restful API]
* [Django Rest_Framework]
  
# API
This application has two main API end-points
The profile end-point `https://mmyawwards.herokuapp.com/api/profile/`
The projects end-point `https://mmyawwards.herokuapp.com/api/projects/`

## Behavior Driven Development

| __Behavior__  | __Input example__ | __Output example__ |
| ------------- | ----------------- | ------------------ |
| The user should see the landing page on first sight | "https://mmyawwards.herokuapp.com/"   | Home  |
| The application should provide an option to register or login to the app | login/register | true  |
| The application should authenticate Users base on details the user provides   | password/username |  access or no access |
| The user should be redirected to home page once logged in | access | home page |
| The user should view different views or post or and projects from different people | --- | Projects |
| The application should be able to restrict unauthorized users from accessing some parts of the application | view | true/false |
| The user should be able to update his/her profile any time | profile update | True |
| The user should be able to view other users who have rated the project | rate | all list |
| The user should be able to review and rate other projects  | rate/review | True |
| The user should be able to logout at will | logout | True |
 
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [lourine.millicent@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Lourine/Awwards/blob/master/LICENSE)  
* Copyright (c) 2020 **Lourine Millicent**