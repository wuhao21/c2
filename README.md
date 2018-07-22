# Ve475 Challenge2 Website

This websites is for UM-SJTU Joint Institute VE475 challenge 2 competition. For more details please check c2 description

## Introduction

The website is written in Django, which is a python open source web framework. If you are new in Django (or python), please first have a look at [Django guide](https://www.djangoproject.com)

Server environment: Python 3.5, Django 1.10.7, gcc/g++ 6.0

Operating System: Linux 4.9.0-6-amd64 #1 SMP Debian 4.9.88-1+deb9u1 (2018-05-07) x86_64 GNU/Linux

Database: Mysql

Server: Nginx

Middleware: gunicorn

## Installation and Deployment Guide
Since the server may be equipped with different version of operating system (maybe ubuntu or centOS) and the package may be updated with time going on. The command ands below may not be working anymore.

**If the following command doesn't work, please search on how to install in different environment**

* Install nginx, mysql, gcc/g++, python3, django
```
$apt-get install mysql-server

$apt-get install python3 gcc g++ nginx python3-django
```
* Put the project folder under your home directory, cd into the project directory

* Install the python dependencies in the projects

```
$pip3 install -r requirements.txt
```
* Start your mysql server
```
$ service mysql start
```
* Log into your mysql, create a new user and a new database named 'c2'
* open c2/settings.py and check whether the database setting corresponds to your mysql settings. If not, modify it.
* migrate the database

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

* Test whether your website is working

```
$ python3 manage.py runserver
```
Then log onto localhost:8000 to see whether it is working.

#### Deployment with nginx and gunicorn.

Since the django server is only the test server and cannot be put into production. After testing the website, we need to deploy it onto nginx.

* Add the following configuration into your nginx config file (OS dependent. For debian: create a file in /etc/nginx/site-enabled/c2.conf and append the following)

```
upstream c2 {
    server unix:/home/ta/c2/run/gunicorn.sock fail_timeout=0;
}

server {

    server_name c2;
    root /home/ta/c2;

    listen 8000;

    keepalive_timeout 70;
    access_log /var/log/nginx/c2_access.log;
    error_log /var/log/nginx/c2_error.log;

    location / {
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

         proxy_set_header Host $http_host;

         proxy_redirect off;


        if (!-f $request_filename) {
            proxy_pass http://c2;
            break;
        }
    }
}
```
This file is also saved in the bin/c2.conf

* open bin/gunicorn_start and modify the user configuration according to your project settings.
* set the file gunicorn_start to executable
```
chmod u+x bin/gunicorn_start
```
* restart your nginx and run the bash file above:
```
$ service nginx restart
$ ./bin/gunicorn_start
```
* log on to localhost:8000 to see if its working.
## Important Notes for Security

In 2018 Summer. This server was compromised because of security breach. This section serves as reminders for future contributors to prevent the server from being broken.

The case of 2018 Summer:

1. TA didn't switched off the debug = True in settings.py. When meeting error, student can directly get the code around the exception. Then the code injection was allowed in the page group/detail.html.

Student entered aaa\' && *any command* && ls\' into the "text" input and the *any command* could be executed

2. TA ran the gunicorn middleware under *root* user. Which will allow everything executed by the outside.

Student could get control of the server.

##### What TA have done in the code to improve the safety:

* Filter any input out of the alphabet, such as \', \!, \&, etc. using regular expression

##### What TA should do when deploying:

* Never run gunicorn_start as *root*
* Create new users in mysql instead of root users and grant privileges to only the c2 database
* Switch off outside connection in mysql
* Switch off Debug mode in Django settings.py
* Install softwares using *apt-get* to get the official package


## Improvement in the future

1. Upgrade the django into 2.x.x
2. Setting the site into https for the sake of security
3. Decoupling of front end and back end
4. The admin site should be improved and made easier to use

## Contributors and Update Log

2017 Summer: Site written by [Wu Hao](https://github.com/wuhao21)

---
2018 Summer: Improvement by Zhu Chen

* Fixed the bug that everyone could input ciphertext to break the cipher
* Created the leaderboard section
* Fixed the security issue
* Change the appearance of the website
* Created this document

---
