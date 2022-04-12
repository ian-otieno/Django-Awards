# Django-Awards
This Python dJango awards web application was created on 11/04/2022

 ## Author
## By **[ IAN OTIENO](https://github.com/ian-otieno)**

## Description
This is a django application where users can posts their projects and have them rated according to usabilty, design and content

## User Stories
These are the behaviours/features that the application implements for use by a user and writer.

* User loads the application using the url provided
* User signs up for the application and taken to login page
* User logs in using the his/her credentials
* User views projects posted by other users
* user posts new projects
* user rates or reviews other projects 
* avaerage score for the project is recorded




## Behaviour Driven Development
## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| users loads the application | *On page load* | login page is loaded |
| user chooses to sign up if does not have an already created sccount | *On  click* | on successful sign up, the user is taken to login page|
| user logs in using the correct credentials | *on page load* | home page is loaded and the user sees various photos on the page |
| user clicks on profile| *On page load* | profile info is loaded showing user info such as username, profile photo, email and phone numbber and the projects the user has posted|
|user chooses to delete a photo| *delete page is loaded*| user chooses to cancel r delete the project|
| user clicks on logout  | *on page load* | user is logged out of the application and taken login page |



## Prerequisites
* Python3.8

## Setup/Installation Requirements
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/ian-otieno/Django-Awards.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Known Bugs

No known bugs

## Technologies Used
- Python3.8
- Django
- Heroku

## Contacts
Email: ian.otieno@student.moringaschool.com

 &#169; 2022 Ian Otieno
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)