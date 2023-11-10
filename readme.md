# Big O Community Web Application
This page is for the Big O Community, a group of people who contribute to and maintain forks of Big O and promote free software and open source knowledge.

# How to setup
## setup user environment (optional)
### create a user environment
> python -m venv env
### activate the environment
> source env/bin/activate

## install the dependencies
> pip install -r requirements.txt

## setup the database environment variables
### you will need to setup foru database environment variables
>```HOST_NAME``` = host name consist of url to he server where the database is hosted 

>```DATABASE_NAME``` = the name of the database to store data

>```USER_NAME``` = username for the database

>```PASSWORD``` = password for the database

### also create a super user account to manage all the information in the database using
>python manage.py createsuperuser
## start the application server for preview
> python3 manage.py runserver